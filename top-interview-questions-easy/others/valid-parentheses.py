"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        opening = deque()

        openings = {"{": "}", "[": "]", "(": ")"}
        closings = {"}": "{", "]": "[", ")": "("}

        for char in s:
            if char in openings:
                opening.append(char)
            elif char in closings:
                if len(opening) == 0:
                    return False
                bracket = opening.pop()
                if char != openings[bracket]:
                    return False

        if len(opening) != 0:
            return False

        return True