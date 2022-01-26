"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums) -> int:
        nums = sorted(nums)
        print(nums)
        i = 0
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 2
        return nums[i]
