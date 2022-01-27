"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        def getLevelOrder(root, lists, index):
            if root is None:
                return

            if len(lists) == index:
                lists.append([])

            currentList = lists[index]
            currentList.append(root.val)

            getLevelOrder(root.left, lists, index + 1)
            getLevelOrder(root.right, lists, index + 1)

        lists = []
        getLevelOrder(root, lists, 0)
        return lists