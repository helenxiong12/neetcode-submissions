# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit >= 10:
                carry = 1
                digit -= 10
            else:
                carry = 0
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            digit = carry + l1.val
            if digit >= 10:
                carry = 1
                digit -= 10
            else:
                carry = 0
            curr.next = ListNode(digit)
            l1 = l1.next
            curr = curr.next
        while l2:
            digit = carry + l2.val
            if digit >= 10:
                carry = 1
                digit -= 10
            else:
                carry = 0
            curr.next = ListNode(digit)
            l2 = l2.next
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummy.next


            
