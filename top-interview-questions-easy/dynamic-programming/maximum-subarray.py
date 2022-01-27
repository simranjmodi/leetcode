"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        currentsub = maxsub = nums[0]

        if len(nums) == 1:
            return nums[0]

        # dp = [-2,-1]
        i = 1
        while i < len(nums):
            currentsub = max(nums[i], currentsub + nums[i])
            maxsub = max(maxsub, currentsub)

            i += 1

        return max(currentsub, maxsub)