"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def isValidBST_aux(root, low=-math.inf, high=math.inf):
            if root is None:
                return True
            elif root.val <= low or root.val >= high:
                return False
            else:
                return isValidBST_aux(root.left, low, root.val) and isValidBST_aux(root.right, root.val, high)

        return isValidBST_aux(root)



