"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        # allocate listnodes 
        nodes = {}
        curr = head
        while curr:
            nodes[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next

        curr = head
        while curr:
            tmp_next = nodes[curr].next
            tmp_random = nodes[curr].random
            if tmp_next:
                nodes[curr].next = nodes[tmp_next]
            if tmp_random:
                nodes[curr].random = nodes[tmp_random]
            curr = curr.next
        return nodes[head]
