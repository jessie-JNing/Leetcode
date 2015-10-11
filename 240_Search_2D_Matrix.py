#!/usr/bin/env python
# encoding: utf-8

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        start, end = 0, (col*row)-1

        while start <= end:
            mid = (start + end)/2
            mid_row, mid_col = divmod(mid, col)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

if __name__=="__main__":
    solution_obj = Solution()

    matrix = [[1,4],[2,5]]
    for k in range(1):
        print solution_obj.searchMatrix(matrix, 2)