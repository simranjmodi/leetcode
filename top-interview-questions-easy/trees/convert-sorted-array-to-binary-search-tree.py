"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def recurseArray(nums):

            total = len(nums)

            # single item in list
            if total == 1:
                node = TreeNode(nums[0])
                return node

            # odd total
            mid = (total // 2)

            node = TreeNode(nums[mid])
            node.left = recurseArray(nums[:mid])
            if mid + 1 < total:
                node.right = recurseArray(nums[mid + 1:])
            return node

        return recurseArray(nums)