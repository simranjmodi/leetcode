"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return False
        n = len(matrix)

        for layer in range(n//2):
            first = layer
            last = n - 1 - layer
            for i in range(first,last):
                offset = i - first
                top = matrix[first][i] # save top

                # left -> top
                matrix[first][i] = matrix[last-offset][first]

                # bottom -> left
                matrix[last-offset][first] = matrix[last][last-offset]

                # right -> bottom
                matrix[last][last-offset] = matrix[i][last]

                # top -> right
                matrix[i][last] = top
