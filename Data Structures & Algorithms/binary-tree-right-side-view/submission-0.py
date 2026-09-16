# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            tmp = []
            for q in queue:
                if q.left:
                    tmp.append(q.left)
                if q.right:
                    tmp.append(q.right)
            res.append(queue[-1].val)
            queue = tmp
        return res


        