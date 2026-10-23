"""Small integration fixture. Usage: python validate_fixture.py OUTPUT_DIRECTORY."""
import json
import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from _common import CliError, checked_input_file
from figure_export import export_figure
from image_metadata import inspect_file
from palette_audit import contrast_ratio
from style_presets import style_context
from export_plan import build_plan

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
# Three subjects; both conditions are paired. Missing time 2 stays a gap.
baseline = np.array([1., 2., 3.]); treatment = np.array([2., 4., 6.])
delta = treatment - baseline
assert delta.mean() == 2.0
assert delta.std(ddof=1) == 1.0
# Resample complete subjects, preserving pairing. Fixed RNG for reproducibility.
rng = np.random.default_rng(20261005)
means = delta[rng.integers(0, 3, size=(10000, 3))].mean(axis=1)
lo, hi = np.quantile(means, [.025, .975])
assert lo == 1.0 and hi == 3.0
old_font = plt.rcParams['font.size']
with style_context('default'):
    fig, axes = plt.subplots(1, 2, figsize=(7, 2.8), layout='constrained')
    line, = axes[0].plot([0, 1, 2, 3], [1, 2, np.nan, 4], marker='o')
    axes[0].set(xlabel='Time (hours)', ylabel='Response (a.u.)', title='A  Missing observation = gap')
    assert np.isnan(line.get_ydata()[2])
    axes[1].scatter([0]*3, delta, marker='o', color='#0072B2', label='Subject differences')
    axes[1].errorbar([.25], [delta.mean()], yerr=[[delta.mean()-lo],[hi-delta.mean()]], fmt='s', color='black', capsize=4, label='Mean and 95% CI')
    axes[1].axhline(0, color='0.6', linewidth=.7)
    axes[1].set(xlim=(-.3,.6), xticks=[], ylabel='Paired change (a.u.)', title='B  Subject bootstrap; n = 3')
    axes[1].legend(loc='lower right', fontsize=7)
    report = export_figure(fig, out/'fixture', formats=['png','pdf','svg'], dpi=150, write_manifest=True, provenance={'data':'synthetic fixture, not experimental evidence','paired_differences':delta.tolist(),'uncertainty':'95% percentile bootstrap CI; n=3 subjects; 10000 resamples; seed=20261005','missing':'time 2 remains NaN'})
assert plt.rcParams['font.size'] == old_font
png = inspect_file(out/'fixture.png')['metadata']
assert (png['width_px'], png['height_px']) == (1050,420)
svg = inspect_file(out/'fixture.svg')['metadata']
assert abs(svg['width_mm'] - 177.8) < .01
pdf = inspect_file(out/'fixture.pdf')['metadata']
assert pdf['format'] == 'PDF'
original = (out/'fixture.png').read_bytes()
try:
    export_figure(fig, out/'fixture', formats=['png'])
except CliError:
    pass
else:
    raise AssertionError('existing figure was overwritten')
assert original == (out/'fixture.png').read_bytes()
assert contrast_ratio((0,0,0),(255,255,255)) == 21.0
assert contrast_ratio((255,255,255),(255,255,255)) == 1.0
plan = build_plan('nature', figure_type='combination', width='single', phase='initial')
assert not plan['phase_matches_snapshot']
malformed = out/'entity.svg'; malformed.write_text('<!DOCTYPE svg [<!ENTITY x "bad">]><svg>&x;</svg>')
try:
    inspect_file(malformed)
except CliError:
    pass
else:
    raise AssertionError('entity declaration was accepted')
malformed.unlink()
plt.close(fig)
(out/'validation.json').write_text(json.dumps({'checks':'paired CI, missing gap, scoped style, dimensions, PDF/SVG/PNG export, overwrite refusal, known contrast, phase mismatch, XML entity rejection','status':'pass','versions':report['versions']}, indent=2)+'\n')
print('PASS: scientific figure fixture and helper checks')
