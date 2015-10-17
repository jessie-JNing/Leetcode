#!/usr/bin/env python
# encoding: utf-8

"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28


@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        for i in range(1, 27):
            mapping[chr(64+i)] = i

        num = 0

        for i in range(len(s)):
            num += (26**i * mapping[s[-i-1]])
        return num


if __name__=="__main__":
    test = Solution()
    print test.titleToNumber('GR')