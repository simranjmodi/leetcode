"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def symmetric(root1, root2):
            if root1 is None and root2 is None:
                return True  # both none
            if root1 is None or root2 is None:
                return False  # only 1 none
            return root1.val == root2.val and symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)

        return symmetric(root, root)
