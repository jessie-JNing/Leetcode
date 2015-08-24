#!/usr/bin/env python
# encoding: utf-8

"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def removeElement(self, nums, val):
        nums= filter(lambda x:x!=val, nums)
        #nums = new_nums
        print nums
        return len(nums)

    def removeElement_2(self, nums, val):
        counter = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[counter]=nums[i]
                counter +=1
        nums = nums[:counter]
        return counter


if __name__=="__main__":
    nums_list = [2,1,2]
    nums_list= [4, 5]
    Solution_obj = Solution()

    #Solution_obj.rotate(nums_list, 3)
    print Solution_obj.removeElement(nums_list, 4)