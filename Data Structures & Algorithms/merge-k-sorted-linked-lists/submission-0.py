# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, list1: ListNode, list2: ListNode):
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        print(n)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        i, j = n-1, n-2
        while i > 0 and j > -1:
            print(i, j)
            lists[j] = self.merge(lists[j], lists[i])
            i -= 1
            j -= 1
        return lists[0]