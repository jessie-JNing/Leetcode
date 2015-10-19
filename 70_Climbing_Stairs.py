#!/usr/bin/env python
# encoding: utf-8

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

@author: Jessie
@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n==2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n):
        memo = {}
        if n in memo:
            return memo[n]
        else:
            if n < 3:
                total = n
            else:
                total = self.climbStairs(n-1) + self.climbStairs(n-2)
            memo[n] = total
            return total

    def climbStairs3(self, n):
        memo = {}
        for i in range(1, n+1):
            if i <3:
                memo[i] = i
            else:
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

    def climbStairs4(self, n):
        if n<3:
            return n
        else:
            one_step = 2
            two_step = 1
            total = 0

            for i in range(3,n+1):
                total = one_step + two_step
                one_step = two_step
                two_step = total
            return total

    def climbStairs5(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in xrange(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b


if __name__=="__main__":

    test = Solution()
    print test.climbStairs4(10)
