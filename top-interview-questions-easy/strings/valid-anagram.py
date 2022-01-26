"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)

        if len(s) != len(t):
            return False

        for idx, ch in enumerate(s):
            if count1[ch] != count2[ch]:
                return False
        return True