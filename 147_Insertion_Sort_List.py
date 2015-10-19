#!/usr/bin/env python
# encoding: utf-8

"""
Sort a linked list using insertion sort.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


    def insertionSort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            for i in range(1, len(nums)):
                current = nums[i]
                j = i
                while j >0 and nums[j-1] > current:
                    nums[j] = nums[j-1]
                    j -= 1
                nums[j] = current

            return nums


if __name__=="__main__":

    test = Solution()
    print test.insertionSort([2,7,9,3,1])