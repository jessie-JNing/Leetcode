#!/usr/bin/env python
# encoding: utf-8

"""

Implement the following operations of a queue using stacks.

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4
and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5

        current = l1
        while current:
            print current.val, "->",
            current = current.next

        print "\nafter delete"
        current = l4
        right = current.next
        while right.next:
            current.val = right.val
            current = right
            right = right.next

        current.val = right.val
        current.next = None

        current = l1
        while current:
            print current.val, "->",
            current = current.next



if __name__=="__main__":

    delete_node = ListNode(3)
    test_solution = Solution()
    test_solution.deleteNode(delete_node)


