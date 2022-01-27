"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums) -> int:

        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, i, nums):

        # No more houses left to examine.
        if i >= len(nums):
            return 0

        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # Cache for future use.
        self.memo[i] = ans
        return ans