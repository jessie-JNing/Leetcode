#!/usr/bin/env python
# encoding: utf-8

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

@author: Jessie

@email: jessie.JNing@gmail.com
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        link = []
        while head:
            link.append(head.val)
            head = head.next
        n = len(link)
        for i in range(n/2):
            if link[i] != link[n-i-1]:
                return False
        return True


if __name__=="__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(2)
    a4 = ListNode(1)
    a5 = ListNode(1)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = None

    test_solution = Solution()
    print test_solution.isPalindrome(a1)