import pytest
from algorithms.arrays.two_pointer import Solution, Solution2, Solution3


@pytest.mark.parametrize("input_str,expected", [
    ("rac tar", "car rat"),
    ("Hello World", "olleH dlroW"),
    ("Python", "nohtyP"),
])
def test_reverse_words(input_str, expected):
    assert Solution.reverseWords_manual(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("I evol edocteel", "I love leetcode"),
])
def test_reverse_words1(input_str, expected):
    assert Solution2.reverserWords(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
])
def test_reverse_words2(input_str, expected):
    assert Solution3.reverseWords_manual1(input_str) == expected
