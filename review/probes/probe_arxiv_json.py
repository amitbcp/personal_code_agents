"""Offline probe of selected arXiv parser functions; no upstream imports or network."""
import ast
import argparse
import contextlib
import io
import json
from pathlib import Path
import types
import urllib.parse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('checkout', type=Path, help='Pinned google-deepmind/science-skills checkout')
source = parser.parse_args().checkout / 'skills/literature_search_arxiv/scripts/search_arxiv.py'
tree = ast.parse(source.read_text())
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in {'strip_namespace', 'search_arxiv'}]
module = ast.Module(body=functions, type_ignores=[])
results = []
for count in (0, 1, 2):
    xml = '<feed xmlns="http://www.w3.org/2005/Atom">' + ''.join(f'<entry><id>https://arxiv.org/abs/1234.0000{i}</id><title>Fixture {i}</title></entry>' for i in range(count)) + '</feed>'
    scope = {'argparse': types.SimpleNamespace(Namespace=types.SimpleNamespace), 'json': json, 'urllib': urllib, 'ET': ET, '_BASE_URL': 'https://example.invalid/', '_CLIENT': types.SimpleNamespace(fetch_bytes=lambda url: xml.encode())}
    exec(compile(module, str(source), 'exec'), scope)
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        scope['search_arxiv'](types.SimpleNamespace(query='fixture', id_list=None, start=0, max_results=10, sort_by=None, sort_order=None))
    try:
        parsed = json.loads(output.getvalue())
        outcome = 'single JSON document'
    except json.JSONDecodeError as error:
        outcome = error.msg
    results.append({'fixture_entries': count, 'outcome': outcome})
print(json.dumps(results, indent=2))
