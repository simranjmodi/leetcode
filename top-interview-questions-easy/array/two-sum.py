"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            if hashmap.get(nums[i]) is not None:
                count = hashmap.get(nums[i])[1]
            else:
                count = 0
            hashmap[nums[i]] = (i, count + 1)

        for i in range(len(nums)):
            difference = target - nums[i]
            if hashmap.get(difference) is not None:
                if difference == nums[i]:
                    if hashmap[difference][1] > 1:
                        return sorted([hashmap[difference][0], i])
                else:
                    return sorted([hashmap[difference][0], i])
