#!/usr/bin/env python
# encoding: utf-8

"""

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

@author: Jessie

@email: jessie.JNing@gmail.com
"""


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p, p1, p2 = head, l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next,p1 = p1, p1.next
            else:
                p.next,p2 = p2, p2.next
            p = p.next

        while p1:
            p.next, p1 = p1, p1.next
            p = p.next

        while p2:
            p.next, p2 = p2, p2.next
            p = p.next

        return head.next

    def mergeTwoLists_2(self, l1, l2):
        if (l1 is None) and (l2 is None):
            return None
        elif l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists_2(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists_2(l1, l2.next)
                return l2
        else:
            return l1 if l1 else l2



if __name__=="__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    b1 = ListNode(9)
    b2= ListNode(8)
    c1 = ListNode(18)
    c2 = ListNode(28)
    a1.next = a2
    b1.next = b2
    a2.next = c1
    b2.next = c1
    c1.next = c2

    test_solution = Solution()
    merge_head = test_solution.mergeTwoLists(a1, b1)


