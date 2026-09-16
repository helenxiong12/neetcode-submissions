# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return

        def recurse(node, maxval): # return num of good nodes in this path
            if not node:
                return 0

            lt = recurse(node.left, max(node.val, maxval))
            rt = recurse(node.right, max(node.val, maxval))

            if node.val >= maxval:
                # this is a good node
                return 1 + lt + rt
            else:
                return lt + rt
        return recurse(root, root.val)