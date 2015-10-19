#!/usr/bin/env python
# encoding: utf-8

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        else:
            need_len = len(needle)
            for i in range((len(haystack)-need_len)+1):
                haydle = haystack[i:(i+need_len)]
                if haydle == needle:
                    return i
            return -1


if __name__=="__main__":

    solution_obj = Solution()
    print solution_obj.strStr('mississppi', 'pi')
