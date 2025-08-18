from typing import Optional
from ListNode import ListNode, create_linked_list, print_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list  = None
        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node
        return new_list
    

reverse_list = Solution()
head = create_linked_list([1,2,3,4,5])


reversed_head = reverse_list.reverseList(head)

print_linked_list(reversed_head)
        