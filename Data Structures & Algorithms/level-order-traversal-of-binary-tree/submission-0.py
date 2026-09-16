# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        search = [root]
        res = []

        while len(search) > 0:
            res.append([s.val for s in search])
            next_lvl = []
            for r in search:
                if r.left: 
                    next_lvl.append(r.left)
                if r.right:
                    next_lvl.append(r.right)
            search = next_lvl

        return res            