#!/usr/bin/env python
# encoding: utf-8

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.divided_five(n, 5)

    def divided_five(self, n, k):
        if n/k <1:
            return 0
        else:
            return self.divided_five(n, 5*k) + n/k

    def trailingZeroes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 5
        zeroes = 0
        while n/k >= 1:
            zeroes += n/k
            k *= 5
        return zeroes






if __name__ == "__main__":

    test = Solution()
    print test.trailingZeroes2(111)