#!/usr/bin/env python
# encoding: utf-8

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.

Make change in place can start from the end of the array


@author: Jessie
@email: jessie.JNing@gmail.com
"""


class Solution(object):

    def merge_3(self, nums1, m, nums2, n):
        i, j = m-1, n-1
        counter = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[counter] = nums1[i]
                i -= 1
            else:
                nums1[counter] = nums2[j]
                j -= 1

            counter -= 1

        while j >= 0:
            nums1[counter] = nums2[j]
            counter -= 1
            j -=1
        return nums1






if __name__=="__main__":
    L1 = [1,3,5,7, 0]
    L2 = [2,4,6,8]
    L2 = [3]
    Solution_obj = Solution()
    print Solution_obj.merge_3(L1, 4, L2, 1)