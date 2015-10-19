#!/usr/bin/env python
# encoding: utf-8

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(x) for x in str(num)]
        dig_sum = sum(digits)
        if dig_sum < 10:
            return dig_sum
        else:
            return self.addDigits(dig_sum)

    def addDigits2(self, num):

        while num > 9:
            digits = [int(x) for x in str(num)]
            num = sum(digits)
        return num

    def addDigits23(self, num):
        if num == 0:
            return 0
        else:
            return 1 + (num - 1)%9


if __name__=="__main__":

    test = Solution()
    print test.addDigits2(38)
