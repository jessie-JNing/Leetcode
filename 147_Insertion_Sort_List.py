#!/usr/bin/env python
# encoding: utf-8

"""
Sort a linked list using insertion sort.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            guard = ListNode(0)
            current = head
            previous = guard
            while current:
                temp = current.next
                while previous.next and previous.next.val < current.val:
                    previous = previous.next

                current.next = previous.next
                previous.next = current

                previous = guard
                current = temp

            return guard.next
        else:
            return head

    def insertionSort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            for i in range(1, len(nums)):
                current = nums[i]
                j = i
                while j >0 and nums[j-1] > current:
                    nums[j] = nums[j-1]
                    j -= 1
                nums[j] = current

            return nums



if __name__=="__main__":

    test = Solution()
    print test.insertionSort([2,7,9,3,1])

    a1 = ListNode(5)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(7)
    a5 = ListNode(1)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    head_node = test.insertionSortList(a1)


    while head_node:
        print head_node.val, "->",
        head_node = head_node.next
