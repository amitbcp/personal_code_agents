"""Bounded demonstration of imported PBT generation/shrinking guidance."""
import unicodedata
from hypothesis import given, strategies as st, settings, find

@given(st.text())
@settings(max_examples=100, deadline=500)
def normalization(value):
    result = unicodedata.normalize('NFC', value)
    assert unicodedata.normalize('NFC', result) == result

normalization()
counterexample = find(
    st.text(alphabet=' a', min_size=1, max_size=10),
    lambda value: value.removeprefix(' ').removeprefix(' ') != value.removeprefix(' '),
)
assert counterexample.startswith('  ')
print(f'NFC idempotence: 100 cases passed; defective normalizer shrank to {counterexample!r}')
