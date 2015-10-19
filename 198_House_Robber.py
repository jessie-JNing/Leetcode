#!/usr/bin/env python
# encoding: utf-8

"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight
without alerting the police.


@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        elif len(nums) < 3:
            return max(nums)

        else:
            passed = {}
            maximum = 0

            for i in range(len(nums)-2):
                for j in range(i, len(nums)):
                    if j < i+2:
                        if j not in passed:
                            if nums[j] > maximum:
                                maximum = nums[j]
                            passed[j] = nums[j]
                    else:
                        if (i,j) not in passed:
                            total = nums[i] + nums[j]
                            if total > maximum:
                                maximum = total
                            passed[(i,j)] = total

            return maximum


if __name__=="__main__":

    test = Solution()
    print test.rob([2,7,9,3,1])
