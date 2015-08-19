#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

@author: Jessie
@email: jessie.JNing@gmail.com
"""

import time

class Solution:
    # @return a tuple, (index1, index2)
    def __init__(self):
        pass


    def twoSum_1(self, num, target):
        flag = False
        for i in range(len(num)-1):
            for j in range(1, len(num)):
                if num[i]+num[j]==target:
                    flag=True
                    break
            if flag:
                break
        return (i+1, j+1)

    def twoSum_2(self, num, target):
        hash_table = {}
        for i in range(len(num)):
            if target-num[i] in hash_table:
                index1=hash_table[target-num[i]]+1
                index2=i+1
            else:
                hash_table[num[i]]=i
        return (index1, index2)


if __name__=="__main__":
    numbers=[2, 7, 11, 15]
    target=9

    Solution_obj = Solution()

    start = time.time()
    print Solution_obj.twoSum_1(numbers, target)
    end = time.time()
    print (end-start)*1000

    start = time.time()
    print Solution_obj.twoSum_2(numbers, target)
    end = time.time()
    print (end-start)*1000
