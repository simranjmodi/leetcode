"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        # set nth node
        endpointer = head
        for i in range(n):
            endpointer = endpointer.next

        startpointer = head
        previous = None
        while endpointer is not None:
            previous = startpointer
            startpointer = startpointer.next
            endpointer = endpointer.next

        if n == 1: # delete last
            if previous is None:
                head = None
                return head
            previous.next = None
        else:
            if previous is None:
                head = startpointer.next
                return head
            previous.next = startpointer.next

        return head