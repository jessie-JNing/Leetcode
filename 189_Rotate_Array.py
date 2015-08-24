#!/usr/bin/env python
# encoding: utf-8

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def rotate(self, nums, k):
        k%=len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print nums

    def rotate_2(self, nums, k):
        n = len(nums)
        k %= n

        for i in range((n-k)/2):
            nums[i], nums[n-k-i-1] = nums[n-k-i-1], nums[i]
        print nums
        for i in range(k/2):
            nums[n-k+i], nums[n-i-1] = nums[n-i-1], nums[n-k+i]
        print nums
        for i in range(n/2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]
        print nums



if __name__=="__main__":
    nums_list = [2,1,2]
    nums_list= [1,2,3]
    Solution_obj = Solution()

    #Solution_obj.rotate(nums_list, 3)
    Solution_obj.rotate_2(nums_list, 2)





