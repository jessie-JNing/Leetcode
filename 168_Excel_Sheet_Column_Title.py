#!/usr/bin/env python
# encoding: utf-8

"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        mapping = {}
        for i in range(1, 27):
            mapping[i] = chr(64+i)

        return self.calculate(n, mapping)


    def calculate(self, num, mapping):
        if num <27:
            return mapping[num]

        else:
            return self.calculate((num-1)/26, mapping) + mapping[((num-1)%26 + 1)]
            #return self.calculate((num-1)/26, mapping)


if __name__=="__main__":
    test = Solution()
    print test.convertToTitle(200)