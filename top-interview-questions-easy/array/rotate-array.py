"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        old_val = nums[0]

        count = 0
        i = 0
        visited = dict()
        while count <= len(nums):
            # print(count)
            new_index = (i + k) % len(nums)
            # print(visited, new_index, old_val)
            if count != 0 and count != len(nums) and visited.get(new_index) == True:
                i += 1
                old_val = nums[i]
                continue

            temp = nums[new_index]
            nums[new_index] = old_val
            old_val = temp
            visited[new_index] = True
            i = new_index
            count += 1


