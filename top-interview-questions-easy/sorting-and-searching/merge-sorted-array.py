"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        counter = m + n - 1

        if p1 == -1:
            for i in range(n):
                nums1[i] = nums2[i]
            print(nums1, nums2)
            return

        if p2 == -1:
            return

        while counter >= 0:
            print(p1, p2, counter)
            if p2 >= 0 and p1 >= 0 and nums2[p2] >= nums1[p1]:
                nums1[counter] = nums2[p2]
                p2 -= 1
            elif p2 >= 0 and p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[counter] = nums1[p1]
                p1 -= 1
            elif p1 == -1:
                nums1[counter] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[counter] = nums1[p1]
                p1 -= 1

            counter -= 1

        print(nums1)