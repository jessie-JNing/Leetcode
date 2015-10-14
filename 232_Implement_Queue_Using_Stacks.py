#!/usr/bin/env python
# encoding: utf-8

"""

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.size()>0:
            return self.data_stack.pop()
        else:
            return None

    def size(self):
        """
        :rtype: int
        """
        return len(self.data_stack)


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data_stack)==0

    def __str__(self):
        return ','.join([str(x) for x in self.data_stack])


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.forward_stack = Stack()
        self.backward_stack = Stack()


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.empty():
            self.top_value = x
        self.forward_stack.push(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return False
        elif self.forward_stack.size()==1:
            self.forward_stack.pop()
            self.top_value = None
        else:

            while self.forward_stack.size()>1:
                self.backward_stack.push(self.forward_stack.pop())
            self.forward_stack.pop()

            self.top_value = self.backward_stack.pop()
            self.forward_stack.push(self.top_value)
            while self.backward_stack.size()>0:
                self.forward_stack.push(self.backward_stack.pop())


    def peek(self):
        """
        :rtype: int
        """
        return self.top_value

    def empty(self):
        """
        :rtype: bool
        """

        return self.forward_stack.size()==0

    def __str__(self):
        return str(self.forward_stack)

if __name__=="__main__":

    test_queue = Queue()
    # test_queue.push(1)
    # test_queue.push(2)
    # test_queue.push(3)
    # print test_queue
    #
    # test_queue.pop()
    # print test_queue
    # test_queue.pop()
    # print test_queue
    #
    # print test_queue.peek()
    test_queue.push(1)
    test_queue.push(2)
    print test_queue
    test_queue.pop()
    print test_queue
    # test_queue.push(3)
    # test_queue.push(4)
    # test_queue.pop()
    print test_queue.peek()