import pytest
from algorithms.linked_lists.Linked_list import DoublyLinkedList


@pytest.mark.parametrize("values,expected", [
    ([3], [3]),
    ([1, 2, 3], [3, 2, 1]),

])
def test_add_to_front(values, expected):
    dll = DoublyLinkedList()
    for v in values:
        dll.add_to_front(v)
    assert dll.to_list() == expected


@pytest.mark.parametrize("initial,expected_removed,expected_remaining", [
    ([1], 1, []),                    # lista só com 1 elemento
    ([1, 2], 1, [2]),                # remove o primeiro de [1,2]
    ([1, 2, 3], 1, [2, 3]),          # remove o primeiro de [1,2,3]
])
def tesst_remove_from_front(initial, expected_removed, expected_remaining):
    dll = DoublyLinkedList()
    for v in initial():
        dll.add_to_end(v)
    removed = dll.remove_from_front()
    assert removed == expected_removed
    assert dll.to_list() == expected_remaining