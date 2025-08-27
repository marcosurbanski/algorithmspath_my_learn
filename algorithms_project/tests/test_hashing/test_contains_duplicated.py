import pytest
from algorithms_project.algorithms.sliding_window.contains_duplicate import Numsolution


array = [1, 2, 3, 1]
k = 3
result = Numsolution().containnumsNearbyDuplicate(array,k)

@pytest.mark.parametrize("array,k,expected", [
    (array,k,result),
])
def test_contains_duplicated(array, k, expected):
    assert Numsolution().containnumsNearbyDuplicate(array,k) == expected
