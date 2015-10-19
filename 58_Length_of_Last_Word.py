#!/usr/bin/env python
# encoding: utf-8

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if len(words)>0:
            return len(words[-1])
        else:
            return 0



if __name__=="__main__":

    solution_obj = Solution()
    print solution_obj.lengthOfLastWord("Hello World")
