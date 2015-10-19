#!/usr/bin/env python
# encoding: utf-8

"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

@author: Jessie
@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = [x.lower() for x in s if x.isalnum()]
        for i in range(len(clean)/2):
            if clean[i]!= clean[len(clean)-i-1]:
                return False
        return True

    def isPalindrome2(self,s):
        i,j = 0, len(s)-1
        while i<len(s) and j>=0:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1

        return True



if __name__=="__main__":
    test = Solution()
    print test.isPalindrome(" ")
