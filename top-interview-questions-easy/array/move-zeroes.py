"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        i = 0
        # [1,0]

        while i < len(nums):
            while p1 < len(nums) and nums[p1] != 0:
                p1 += 1
            # now pos p1 has 0
            while i < len(nums) and nums[i] == 0:
                i += 1
            # now i has number
            # print(p1,i)
            if i < len(nums) and p1 < len(nums) and p1 < i:
                nums[p1], nums[i] = nums[i], nums[p1]
            i += 1
            # print(nums)

