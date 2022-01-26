"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        hashmap = dict()
        for num in nums1:
            val = hashmap.get(num)
            if val is not None:
                val += 1
            else:
                val = 1
            hashmap[num] = val

        k = 0
        for num in nums2:
            val = hashmap.get(num)
            if val is not None and val > 0:
                nums1[k] = num
                k += 1
                hashmap[num] = val - 1

        return nums1[:k]
