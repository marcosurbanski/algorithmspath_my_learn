from typing import Optional
from ListNode import ListNode, create_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # abaixo será  criado uma nova lista vazia (vai ser a lista invertida)
        new_list = None

        # Enquanto ainda existir algum nó (Elemento) na lista original
        while head:
            # Guardamos o próximo nó para não perder o resta da lista

            next_node = head.next

            # Fazemos o nó atual apontar para a nova lista (invertendo a direção)
            head.next = new_list

            # Agora o nó atual passa a ser a cabeça da nova lista
            new_list = head

            # e seguimos para o próximo nó da lista original
            head = next_node
        return new_list


# criamos um "objeto" da classe Solution, que tem o método de inverter a lista
reverse_list = Solution()


# criamos uma lista com os números
head = create_linked_list([1, 2, 3, 4, 5])


# chamamos a função que inverte a lista: vira 5 → 4 → 3 → 2 → 1
reversed_head = reverse_list.reverseList(head)


print_linked_list(reversed_head)
