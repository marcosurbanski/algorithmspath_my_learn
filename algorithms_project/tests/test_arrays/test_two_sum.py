from algorithms.arrays.two_sum import Problem1

def test_two_sum_basic():
    assert sorted(Problem1().two_sum([2, 7, 11, 15], 9)) == [0, 1]

def test_two_sum_none():
    assert Problem1().two_sum([1, 2, 3], 7) == []


def test_example1():
    assert two_sum([1, 2, 3, 4], 5) == [1, 2]

def test_example2():
    assert two_sum([-1, 2, 3, 4], 10) == [-1, -1]

def test_example3():
    assert two_sum([-1, -1, 2, -1], 1) == [1, 2]

def test_no_pair():
    assert two_sum([1, 3, 5], 100) == [-1, -1]

def test_multiple_pairs():
    # Pairs: (0, 3) = 1+4=5; (1,2)=2+3=5
    # j mínimo é 2, entre pares com j=2, i máximo é 1
    assert two_sum([1, 2, 3, 4], 5) == [1, 2]
