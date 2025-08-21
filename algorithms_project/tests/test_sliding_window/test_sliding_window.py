import pytest
from algorithms.sliding_window.sliding_window import Solution


@pytest.mark.parametrize("max,string,expected ", [
    (3, "bcbbbcbaaaaaaabcbdaaddddacbbbbb", 7),
])
def test_binary_search(max, string, expected):
    assert Solution.maximumLengthSubstring(max, string) == expected