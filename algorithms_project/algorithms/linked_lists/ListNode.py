class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def create_linked_list(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

       