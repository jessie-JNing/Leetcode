#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Pay attention to the case input is "[]"

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def summaryRanges(self, nums):
        sum_range = []
        if len(nums)>0:
            sub_range = [nums[0]]
            for i in range(1, len(nums)):
                if sub_range[-1]+1==nums[i]:
                    sub_range.append(nums[i])
                else:
                    sum_range.append(self.sum_string(sub_range))
                    sub_range = [nums[i]]
            sum_range.append(self.sum_string(sub_range))
        return sum_range

    def sum_string(self, sub_nums):
        if len(sub_nums)>1:
            return str(sub_nums[0]) + "->" + str(sub_nums[-1])
        else:
            return str(sub_nums[0])




if __name__=="__main__":
    nums_list = [0,1,2,3,4,5,6,7,8]
    #nums_list= []
    Solution_obj = Solution()

    print Solution_obj.summaryRanges(nums_list)