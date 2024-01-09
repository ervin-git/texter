from __future__ import annotations

from difflib import ndiff


def distance(a: str, b: str) -> int:
    """
    Compute the difference between the two strings
        done by counting the number of changes necessary to
        convert one string to the other
    (aka Levenshtein)
    Returns the distance between the two strings
    """
    change_counter = {"+": 0, "-": 0}
    distance = 0
    for line_diff in ndiff(a, b):
        change = line_diff[0]
        match change:
            # match case, update any changes to max and reset
            case " ":
                distance += max(change_counter.values())
                change_counter = {"+": 0, "-": 0}
            # change case, update the change counter dict
            case _:
                change_counter[change] += 1
    # after final char, we need to update the distance
    distance += max(change_counter.values())
    return distance


def match(a: str, b: str) -> float:
    """
    Returns the percentage of similarity between the two strings
    """
    longest = max(max(len(a), len(b)), 1)
    return 1 - float(distance(a, b)) / longest
