# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_ht = 0
        
        def recurse(node):
            # nonlocal max_ht

            if not node:
                return 0
            lt = recurse(node.left)
            rt = recurse(node.right)
            self.max_ht = max(self.max_ht, lt+rt)
            return 1+max(lt, rt)

        recurse(root)
        return self.max_ht
        