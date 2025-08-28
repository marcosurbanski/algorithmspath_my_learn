import pytest
from algorithms_project.algorithms.linked_lists.Linked_list import DoublyLinkedList


@pytest.mark.parametrize("values,expected", [
    ([3], [3]),
    ([1, 2, 3], [3, 2, 1]),

])
def test_add_to_front(values, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.add_to_front(v)
    assert dll.to_list() == expected
