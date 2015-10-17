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

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        guard = head
        current = head
        while head:
            while current.next:
                if current.val == current.next.val:
                    current = current.next
                else:
                    break
            current = current.next
            head.next = current
            head = head.next
        return guard







if __name__=="__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(2)
    a4 = ListNode(2)
    a5 = ListNode(2)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    test_solution = Solution()

    head_node = test_solution.deleteDuplicates(a1)

    while head_node:
        print head_node.val, "->",
        head_node = head_node.next
