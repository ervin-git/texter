from __future__ import annotations

from math import isclose

import pytest
from string_diff import distance
from string_diff import match


@pytest.mark.parametrize(
    "a, b, expected",
    [("a", "a", 0), ("ABCD", "AF", 3), ("ABCD", "ABCD", 0), ("", "", 0)],
)
def test_distance(a: str, b: str, expected: int):
    assert expected == distance(a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("a", "a", 1.0),
        ("ab", "ac", 0.5),
        ("", "", 1.0),
        ("abc", "efg", 0.0),
        ("abc", "abcd", 0.75),
        ("abcd", "abce", 0.75),
        ("", "abc", 0.0),
    ],
)
def test_match(a: str, b: str, expected: float):
    assert isclose(match(a, b), expected)
