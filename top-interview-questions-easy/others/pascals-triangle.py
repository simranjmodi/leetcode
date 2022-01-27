"""
Given an integer numRows, return the first numRows of Pascal's triangle.
"""


class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        allRows = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            print(i)
            previousRow = allRows[i - 2]
            currentRow = [1]
            for j in range(1, len(previousRow)):
                currentRow.append(previousRow[j] + previousRow[j - 1])
            currentRow.append(1)
            allRows.append(currentRow)

        return allRows
