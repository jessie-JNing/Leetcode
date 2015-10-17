#!/usr/bin/env python
# encoding: utf-8

"""

Given an integer, write a function to determine if it is a power of two.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        while n%2 == 0:
            n = n/2

        if n == 1:
            return True
        else:
            return False


    def isPowerOfTwo2(self, n):
        if n == 0:
            return True

        n = self.power(n)

        if n == 1:
            return True
        else:
            return False

    def power(self, n):
        k = 2
        while n%k==0:
            n = n/k
            k = k<<1

        if n%2==0:
            return self.power(n)
        else:
            return n





if __name__=="__main__":
    test = Solution()
    print test.isPowerOfTwo(-5)