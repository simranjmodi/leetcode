"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums) -> int:
        total = sum(nums)
        print(total)

        n = len(nums)
        required_total = n * (n + 1) / 2

        return int(required_total - total)