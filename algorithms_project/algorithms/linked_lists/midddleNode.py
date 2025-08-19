from typing import Optional
from ListNode import ListNode, create_linked_list, print_linked_list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Criamos um ponteiro chamado "ahead" que vai andar o dobro da velocidade do "head"
        ahead = head

        # Enquanto o "ahead" não chegar no fim da lista e ainda existir um próximo nó para ele andar ahead.next para não estourar o código
        while ahead and ahead.next:

            # "ahead" anda 2 passos de cada vez
            ahead = ahead.next.next

            # "head" anda 1 passo de cada vez
            head = head.next
        return head

# Criamos um objeto da  classe Solution
middle_node = Solution()

# Criamos uma lista
head = create_linked_list([1,2,3,4,5])

# Chamamos a função para encontrar o meio
middle_node = middle_node.middleNode(head)

print_linked_list(middle_node)