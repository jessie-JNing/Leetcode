#!/usr/bin/env python
# encoding: utf-8

"""

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.


@author: Jessie

@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        while num%2==0:
            num = num/2

        while num%3==0:
            num = num/3

        while num%5==0:
            num = num/5

        if num == 1 or num == -1:
            return True
        else:
            return False



    def isUgly2(self, num):
        num = self.check(num, 2)
        num = self.check(num, 3)
        num = self.check(num, 3)

        if num == 1:
            return True
        else:
            return False

    def check(self, num, factor):
        if num == 0 :
            return num
        while num%factor == 0:
            num = (num/factor)
        return num



if __name__=="__main__":
    test = Solution()
    print test.isUgly(-2147483648)
    # for i in range(50):
    #     print test.isUgly(i)
