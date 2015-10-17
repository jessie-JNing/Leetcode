#!/usr/bin/env python
# encoding: utf-8

"""

Write a program to find the node at which the intersection of two singly
linked lists begins.

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        current = head

        while current:
            mark = current.next
            current.next = prev
            prev = current
            current = mark

        return prev

    def reverseList2(self, head):
        return self._reverse(head)

    def _reverse(self, current, prev=None):
        if not current:
            return prev
        mark = current.next
        current.next = prev
        return self._reverse(mark, current)


if __name__=="__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    test_solution = Solution()

    head_node = test_solution.reverseList2(a1)


    while head_node:
        print head_node.val, "->",
        head_node = head_node.next
