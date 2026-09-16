"""Inventory every tracked upstream file without executing upstream code.

This is mechanical coverage, not a semantic review or security certification.
Pass --sources for the directory containing the six upstream checkouts.
"""
import ast
import argparse
import csv
import json
from pathlib import Path
import re
import subprocess

CUES = {
    "publication": r"push_to_hub|hf upload|git push|publish|upload_folder",
    "external_service": r"OPENAI_API_KEY|ANTHROPIC_API_KEY|OPENROUTER_API_KEY|parallel-cli|modal\.com|hf_jobs|HF Jobs",
    "execution": r"subprocess|os\.system|shell=True|eval\(|exec\(|curl.*\|.*(?:sh|bash)",
    "scope_expansion": r"always use|every (?:task|session)|mandatory|MUST|non-negotiable",
    "machine_assumption": r"/Users/|/home/|sudo |nvidia-smi|\.claude/|/tmp/",
    "license_notice": r"copyright|SPDX-License|license",
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, sources = [], []
    for root in sorted(args.sources.iterdir()):
        if not (root / ".git").exists():
            continue
        def git(*args):
            return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()
        files = [name for name in git("ls-files", "-z").split("\0") if name]
        sources.append({"repository": root.name, "url": git("remote", "get-url", "origin"),
                        "revision": git("rev-parse", "HEAD"), "tracked_files": len(files)})
        for rel in files:
            path = root / rel
            blob = path.read_bytes()
            try:
                body = blob.decode("utf-8")
                if "\0" in body:
                    raise UnicodeError()
            except UnicodeError:
                rows.append([root.name, rel, len(blob), "binary", "", "not parsed"])
                continue
            cues = [name for name, expression in CUES.items() if re.search(expression, body, re.I)]
            syntax = "not applicable"
            if path.suffix == ".py":
                try:
                    ast.parse(body, filename=rel)
                    syntax = "AST parsed; not executed"
                except SyntaxError as error:
                    syntax = f"syntax error line {error.lineno}: {error.msg}"
            rows.append([root.name, rel, len(blob), "text-full-file-cue-scan", ";".join(cues), syntax])
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    with (out / "tracked-files.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["repository", "path", "bytes", "mechanical_coverage", "review_cues", "python_syntax"])
        writer.writerows(rows)
    (out / "sources.json").write_text(json.dumps(sources, indent=2) + "\n")
    print(json.dumps({"sources": len(sources), "files": len(rows),
                      "binary_files": sum(row[3] == "binary" for row in rows),
                      "syntax_errors": sum(row[5].startswith("syntax error") for row in rows)}))

if __name__ == "__main__":
    main()
