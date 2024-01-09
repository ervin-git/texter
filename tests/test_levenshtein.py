from __future__ import annotations

import pytest
from levenshtein import distance


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("a", "a", 0),
    ],
)
def test_distance(a: str, b: str, expected: int):
    assert expected == distance(a, b)
