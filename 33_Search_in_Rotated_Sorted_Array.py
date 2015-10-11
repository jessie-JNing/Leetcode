#!/usr/bin/env python
# encoding: utf-8

"""

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the rotate point, the smallest value in the list
        n = len(nums)
        start, end = 0, n-1
        while start < end:
            mid = (start + end)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid


        # The usual binary search and accounting for rotation.
        rotate_point = start
        start, end = 0, n-1

        while start <= end:
            mid = (start + end)/2
            real_mid = (mid + rotate_point)%n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def search_2(self,  nums, target):
        rotated_point = self.find_rotated(nums)
        print rotated_point
        if nums[rotated_point] == target:
            return rotated_point

        if nums[-1] == target:
            return len(nums)-1

        start = rotated_point if target < nums[-1] else 0
        end = rotated_point if target > nums[-1] else len(nums)-1
        #print start, end


        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def find_rotated(self, rot_nums):
        start, end = 0, len(rot_nums)-1
        while start < end:
            mid = (start + end)/2
            if rot_nums[mid] > rot_nums[end]:
                start = mid + 1
            else:
                end = mid
        return start



if __name__=="__main__":

    rotated = [8,9,2,3,4]
    Solution_obj = Solution()

    for k in range(10):
        #print k, Solution_obj.search_2(rotated, k)
        Solution_obj.search_2(rotated, k)