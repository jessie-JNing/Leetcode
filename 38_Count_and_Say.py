#!/usr/bin/env python
# encoding: utf-8

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = 1
        for i in range(n-1):
            num = self.convertsay(num)

        return str(num)


    def convertsay(self, num):
        digit = [x for x in str(num)]
        say_str = ""
        i = 0
        while i < len(digit):
            j = i + 1
            count = 1
            while j<len(digit) and digit[i] == digit[j]:
                j += 1
                count += 1
            say_str += (str(count) + digit[i])
            i = j

        return say_str




if __name__=="__main__":
    test = Solution()
    print test.countAndSay(5)