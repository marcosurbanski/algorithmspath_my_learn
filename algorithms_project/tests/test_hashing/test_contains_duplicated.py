import pytest
from algorithms.sliding_window.contains_duplicate import Numsolution, Solution


array = [1, 2, 3, 1]
k = 3
result = Numsolution().containnumsNearbyDuplicate(array, k)


@pytest.mark.parametrize("array,k,expected", [
    (array, k, result),
])
def test_contains_duplicated(array, k, expected):
    assert Numsolution().containnumsNearbyDuplicate(array, k) == expected


array = [1, 2, 3, 1]
k = 3
result = Solution().containsnumsNearbyDuplicate2(array, k)


@pytest.mark.parametrize("array,k,expected", [
    (array, k, result),
])
def test_contains_duplicated1(array, k, expected):
    assert Solution().containsnumsNearbyDuplicate2(array, k) == expected
