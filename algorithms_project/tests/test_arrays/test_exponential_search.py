import pytest
from algorithms_project.algorithms.binary_search.exponential_search import Solution


@pytest.mark.parametrize("array,target,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
      14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
      25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
      36, 37, 38, 39, 40], 14, 13),
])
def test_exponential_search(array, target, expected):
    assert Solution().exponencial_search(array, target) == expected


@pytest.mark.parametrize("array,target,expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
])
def test_exponential_search_unknown_size(array, target, expected):
    assert Solution().exponencial_search(array, target) == expected
