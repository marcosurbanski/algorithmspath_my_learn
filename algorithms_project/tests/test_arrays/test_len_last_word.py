import pytest
from algorithms.arrays.len_last_word import Solution, Solution2


@pytest.mark.parametrize("string_word,expected", [
    ("Hello World", 5),
])
def test_lengthOfLastWord(string_word, expected):
    assert Solution().lengthOfLastWord(string_word) == expected

@pytest.mark.parametrize("string_word,expected", [
    ("Hello World", 5),
])
def test_lengthOfLastWord1(string_word, expected):
    assert Solution2().lengthOfLastWord(string_word) == expected
