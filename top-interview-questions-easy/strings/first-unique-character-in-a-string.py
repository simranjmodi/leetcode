"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1