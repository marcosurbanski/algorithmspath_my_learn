import pytest
from algorithms_project.algorithms.arrays.first_uni_char import Solution


st = "leetcode"
ex = Solution().firstUniqChar("leetcode")

@pytest.mark.parametrize("string,expected", [
    (st, ex),
])
def test_exponential_search(string, expected):
    assert Solution().firstUniqChar(string) == expected

st = "loveleetcode"
ex = Solution().firstUniqChar("loveleetcode")

@pytest.mark.parametrize("string,expected", [
    (st, ex),
])
def test_exponential_search1(string, expected):
    assert Solution().firstUniqChar(string) == expected
