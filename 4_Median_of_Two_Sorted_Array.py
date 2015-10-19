#!/usr/bin/env python
# encoding: utf-8

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):

        nums3 = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i <len(nums1):
            nums3.extend(nums1[i:])
        if j < len(nums2):
            nums3.extend(nums2[j:])


        if len(nums3)%2==1:
            return nums3[len(nums3)/2]
        else:
            n = len(nums3)/2
            return (nums3[n-1] + nums3[n])/2.0





if __name__=="__main__":

    test = Solution()
    print test.findMedianSortedArrays([1,2], [1,2])