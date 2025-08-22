import pytest
from algorithms.arrays.len_last_word import Solution


@pytest.mark.parametrize("string_word,expected", [
    ("Hello World", 5),
])
def test_lengthOfLastWord(string_word, expected):
    assert Solution().lengthOfLastWord(string_word) == expected
