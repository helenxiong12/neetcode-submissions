# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(node, text: Optional[string]):
            dummy = node
            s = text + " "
            while dummy:
                s += str(dummy.val) + " "
                dummy = dummy.next
            print(s)

        def reverseList(node):
            prev, curr = None, node
            while curr:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            s = ""
            node = prev
            printList(node, "reverse")
            return node

        def mergeCustom(node1, node2):
            dummy = ListNode()
            curr = dummy
            while node1 and node2:
                curr.next = node1
                node1 = node1.next
                curr = curr.next
                curr.next = node2
                node2 = node2.next
                curr = curr.next
            if node1:
                curr.next = node1
            else:
                curr.next = node2
            printList(dummy.next, "merge")
            return dummy.next

        # count
        count = 0
        ctr = head
        while ctr:
            ctr = ctr.next
            count += 1
        # split at half
        n = math.ceil(count / 2)
        print("split", n)
        ctr = head
        for _ in range(n - 1):
            ctr = ctr.next
        list2 = ctr.next
        ctr.next = None

        list2 = reverseList(list2)
        mergeCustom(head, list2)