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
    # @return a float
    def findMedianSortedArrays(self, nums1, nums2):
        m, n, i, j = len(nums1), len(nums2), 0, 0
        mid = (m+n)/2
        C = []
        while i+j<=mid:
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    C.append(nums1[i])
                    i+=1
                else:
                    C.append(nums2[j])
                    j+=1
            elif i<m and j>=n:
                C.extend(nums1[i:mid-j+1])
                break
            elif i>=m and j<n:
                C.extend(nums2[j:mid-i+1])
                break
        print C
        if (m+n)%2==1:
            return float(C[mid])
        else:
            return (C[mid-1] + C[mid])/2.0





if __name__=="__main__":
    LA = [3]
    LB = [1,2,4,5,6,7]
    Solution_ojb = Solution()
    print Solution_ojb.findMedianSortedArrays(LA, LB)