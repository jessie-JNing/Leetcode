#!/usr/bin/env python
# encoding: utf-8

"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s)%2 ==1:
            return False
        else:
            stack_str = []
            parentheses = {")": "(", "]": "[", "}":"{"}
            for ele in s:
                if ele in parentheses.values():
                    stack_str.append(ele)
                elif ele in parentheses.keys():
                    if len(stack_str)==0 or parentheses[ele]!=stack_str.pop():
                        return False
                else:
                    return False

            return stack_str==[]


if __name__=="__main__":

    solution_obj = Solution()

    print solution_obj.isValid("()[]")