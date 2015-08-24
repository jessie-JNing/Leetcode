#!/usr/bin/env python
# encoding: utf-8

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def getRow(self, rowIndex):
        pastcal_row = [1]
        for row in range(rowIndex):
            pastcal_pre = pastcal_row
            pastcal_row = [1]
            for i in range(len(pastcal_pre)-1):
                pastcal_row.append(pastcal_pre[i]+pastcal_pre[i+1])
            pastcal_row.append(1)
        return pastcal_row


if __name__=="__main__":
    Solution_obj = Solution()
    print Solution_obj.getRow(0)