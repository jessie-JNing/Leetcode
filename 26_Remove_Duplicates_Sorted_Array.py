#!/usr/bin/env python
# encoding: utf-8

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def removeDuplicates(self, nums):
        counter = 0
        if len(nums)>1:
            temp = nums[0]
            for i in range(1, len(nums)):
                if nums[i]!=temp:
                    counter +=1
                    nums[counter] = nums[i]
                    temp = nums[i]
        nums = nums[:counter+1]
        print nums
        return len(nums)

    def removeDuplicates_2(self, nums):
        counter = 1
        if len(nums)>1:
            for i in range(1, len(nums)):
                if nums[i-1]!=nums[i]:
                    nums[counter]=nums[i]
                    counter +=1
        nums = nums[:counter]
        return len(nums)


if __name__=="__main__":
    nums_list = [2,1,2]
    nums_list= [4,4, 5]
    Solution_obj = Solution()

    #Solution_obj.rotate(nums_list, 3)
    print Solution_obj.removeDuplicates(nums_list)