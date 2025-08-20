import pytest
from algorithms.arrays.two_pointer import Solution


@pytest.mark.parametrize("input_str,expected", [
    ("rac tar", "car rat"),
    ("Hello World", "olleH dlroW"),
    ("Python", "nohtyP"),
])
def test_reverse_words(input_str, expected):
    assert Solution.reverseWords_manual(input_str) == expected
