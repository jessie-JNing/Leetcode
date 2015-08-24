#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def majorityElement(self, nums):
        nums = sorted(nums)
        major_num = 1
        for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                major_num += 1
            else:
                if major_num > len(nums)/2:
                    return nums[i-1]
                else:
                    major_num = 1

        if len(nums) >1:
            return nums[i]
        else:
            return nums[0]



if __name__=="__main__":
    L1 = [1,3,5,7, 0]
    L2 = [2,4,6,8]
    L2 = [3,2,3,3]
    #L2 = [1,1]

    Solution_obj = Solution()

    print Solution_obj.majorityElement(L2)