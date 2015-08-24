#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def containsDuplicate(self, nums):
        nums_dic = {}
        for ele in nums:
            if ele in nums_dic:
                return True
            else:
                nums_dic[ele] = 1
        return False

    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums_set)<len(nums):
            return True
        else:
            return False




if __name__=="__main__":
    L1 = [1,3,5,7, 0]
    L2 = [2,4,6,8]
    L2 = [3,2,3,3]
    #L2 = [1,1]

    Solution_obj = Solution()

    print Solution_obj.containsDuplicate(L2)