import pytest
from algorithms_project.algorithms.linked_lists.Linked_list import DoublyLinkedList


n = 3

@pytest.mark.parametrize("n,expected", [
    (n, DoublyLinkedList().current_tail()),
])
def test_contains_duplicated(n,expected):
    assert DoublyLinkedList().add_to_front(n) == expected