#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.


@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        Flag = False
        num_dic = {}
        for i in range(len(nums)):
            if nums[i] in num_dic and i-num_dic[nums[i]]<=k:
                Flag = True
                break
            else:
                num_dic[nums[i]]=i
        return Flag




if __name__=="__main__":
    L1 = [1,3,5,7, 0]
    L2 = [2,4,6,8]
    L2 = [2,2]
    #L2 = [1,1]

    Solution_obj = Solution()

    print Solution_obj.containsNearbyDuplicate(L2,3)