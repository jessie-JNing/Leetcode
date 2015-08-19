#!/usr/bin/env python
# encoding: utf-8

"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

@author: Jessie
@email: jessie.JNing@gmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def __init__(self):
        pass

    def addTwoNumbers1(self, l1, l2):
        l3 = cur_3= ListNode(0)
        add1 = 0
        cur_1, cur_2 = l1, l2

        while cur_1 or cur_2:
            v1 = cur_1.val if cur_1 else 0
            v2 = cur_2.val if cur_2 else 0

            add1, v3 = divmod(v1 + v2 + add1, 10)
            cur_3.next = ListNode(v3)
            cur_1 = cur_1.next if cur_1 else cur_1
            cur_2 = cur_2.next if cur_2 else cur_2
            cur_3  = cur_3.next

        if add1>0:
            cur_3.next = ListNode(1)

        return l3.next



if __name__=="__main__":

    L11, L12, L13 = ListNode(2), ListNode(4), ListNode(3)
    L11.next= L12
    L12.next= L13

    L21, L22, L23 = ListNode(5), ListNode(6), ListNode(6)
    L21.next= L22
    L22.next= L23

    Solution_obj = Solution()
    ll =  Solution_obj.addTwoNumbers1(L11, L21)

    cur = ll
    while cur:
        #print ll.next
        print "solution", cur.val
        cur = cur.next
