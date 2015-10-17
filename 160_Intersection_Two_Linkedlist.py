#!/usr/bin/env python
# encoding: utf-8

"""

Write a program to find the node at which the intersection of two singly
linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        while headA:
            current_B = headB
            while current_B:
                if headA == current_B:
                    return headA.val
                else:
                    current_B = current_B.next
            headA = headA.next

        return None


    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        i = 0
        currentA, currentB = headA, headB

        while currentA or currentB:
            if currentA is None:
                i -= 1
                currentB = currentB.next
            elif currentB is None:
                i += 1
                currentA = currentA.next
            else:
                currentA = currentA.next
                currentB = currentB.next

        currentA, currentB = headA, headB
        while currentA and currentB:
            if i < 0:
                currentB = currentB.next
                i += 1
            elif i > 0:
                currentA = currentA.next
                i -= 1
            else:
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next
        return None



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
    print test_solution.getIntersectionNode2(a1, b1)


