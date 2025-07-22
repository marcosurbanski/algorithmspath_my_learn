from algorithms.arrays.two_sum import two_sum

def test_two_sum_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]

def test_two_sum_none():
    assert two_sum([1, 2, 3], 7) == []
