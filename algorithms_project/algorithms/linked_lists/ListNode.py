class ListNode:
    def __init__(self, val=0, next=None):
        # Cada "nó" da lista tem um valor (val)
        self.val = val

        # E uma referência para o próximo nó (next)
        self.next = next


def create_linked_list(lst):
    head = None

    # Percorremos a lista original de trás para frente
    for val in reversed(lst):
        # Cada novo valor vira a cabeça da lista
        head = ListNode(val, head)
    return head


def print_linked_list(head):
    values = []
    while head:
        # Pegamos o valor do nó atual e adicionamos na lista Python
        values.append(head.val)
        # Andamos para a o próximo nó
        head = head.next
    print(values)
