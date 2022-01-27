"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = (x ^ y)
        distance = 0
        while xor != 0:
            if xor & 1 != 0:
                distance += 1
            xor >>= 1

        return distance
