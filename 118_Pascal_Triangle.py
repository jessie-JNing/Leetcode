#!/usr/bin/env python
# encoding: utf-8

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def generate(self, numRows):
        if numRows<1:
            return []
        else:
            pascal = [[1]]
            for row in range(1, numRows):
                pascal.append([1])
                for i in range(len(pascal[row-1])-1):
                    pascal[row].append(pascal[row-1][i] + pascal[row-1][i+1])
                pascal[row].append(1)
            return pascal


if __name__=="__main__":
    Solution_obj = Solution()
    print Solution_obj.generate(1)