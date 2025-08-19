from algorithms.arrays.two_sum import Problem1

def test_two_sum_basic():
    assert sorted(Problem1().two_sum([2, 7, 11, 15], 9)) == [0, 1] # Vai retornar os indices 0 e 1 devido a soma de 2 e 7

def test_example1():
    assert Problem1().two_sum([1, 2, 3, 4], 5) == [1, 2] # Vai retornar os indices 1 e 2 devido a soma de 2 e 3

def test_example2():
    assert Problem1().two_sum([-1, 2, 3, 4], 10) == [-1, -1] # Vai retornar os indices -1 e -1 devido a soma de todos os indices não chegar a 10

def test_example3():
    assert Problem1().two_sum([-1, -1, 2, -1], 1) == [1, 2] # Vai retornar os indices 1 e 2 devido a soma de -1 + 2 chegar a 1


def test_no_pair():
    assert Problem1().two_sum([1, 3, 5], 100) == [-1, -1]  # Vai retornar os indices -1 e -1 devido a soma de todos os indices não chegar a 100
