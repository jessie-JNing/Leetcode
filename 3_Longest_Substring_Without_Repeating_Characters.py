#!/usr/bin/env python
# encoding: utf-8

"""
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.

@author: Jessie
@email: jessie.JNing@gmail.com
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        start, max_len = 0, 0
        hash_s = {}
        for i in range(len(s)):
            if s[i] in hash_s:
                start = hash_s[s[i]] + 1
            hash_s[s[i]]=i

            if i-start+1>max_len:
                max_len= i-start+1
        return max_len

if __name__=="__main__":
    Solution_obj = Solution()
    test_s = "abcabcbb"

    print Solution_obj.lengthOfLongestSubstring(test_s)