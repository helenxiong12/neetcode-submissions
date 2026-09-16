# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # iterate node
        first, second = head, head
        for _ in range(n):
            second = second.next 
        if not second: # remove end of list 
            head = first.next
        else:
            while second.next:
                first = first.next
                second = second.next
            first.next = first.next.next

        return head
