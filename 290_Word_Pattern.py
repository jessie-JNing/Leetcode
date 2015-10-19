#!/usr/bin/env python
# encoding: utf-8

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase
letters separated by a single space.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) == len(pattern):
            forwards = {}
            backwards = {}
            for i in range(len(words)):
                if words[i] in forwards:
                    if forwards[words[i]] != pattern[i]:
                        return False
                else:
                    forwards[words[i]] = pattern[i]

                if pattern[i] in backwards:
                    if backwards[pattern[i]] != words[i]:
                        return False
                else:
                    backwards[pattern[i]] = words[i]
            return True
        else:
            return False

    def wordPattern2(self, pattern, str):
        d = {}
        s = str.split()
        if len(s) != len(pattern):
            return False

        for i, n in enumerate(pattern):
            print i, n
            if n not in d:
                d[n] = s[i]
            elif d[n] != s[i]:
                return False
        return len(d) == len(set(d.values()))


if __name__=="__main__":

    test = Solution()
    print test.wordPattern2("abba", "dog cat cat fish")