#!/usr/bin/env python
# encoding: utf-8

"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

@author: Jessie

@email: jessie.JNing@gmail.com
"""


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_queue = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data_queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.data_queue)>0:
            return self.data_queue.pop(0)
        else:
            return False

    def size(self):
        """
        :rtype: int
        """
        return len(self.data_queue)


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data_queue)==0

    def __str__(self):
        return ','.join([str(x) for x in self.data_queue])


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.forward_queque = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.forward_queque.push(x)
        self.top_value = x

    def pop(self):
        """
        :rtype: nothing
        """
        if self.forward_queque.size()==0:
            return False
        else:
            for i in range(self.forward_queque.size()-1):
                if i ==self.forward_queque.size()-2:
                    self.top_value = self.forward_queque.pop()
                    self.forward_queque.push(self.top_value)
                else:
                    self.forward_queque.push(self.forward_queque.pop())
            self.forward_queque.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.forward_queque.size()==0:
            return False
        # else:
        #     for i in range(self.forward_queque.size()-1):
        #         self.forward_queque.push(self.forward_queque.pop())
        #     top_value = self.forward_queque.pop()
        #     self.forward_queque.push(top_value)
        #     return top_value
        return self.top_value


    def empty(self):
        """
        :rtype: bool
        """
        return self.forward_queque.size()==0

    def __str__(self):
        return str(self.forward_queque)



if __name__=="__main__":



    test_stack = Stack()
    test_stack.push(11)
    test_stack.push(22)
    test_stack.push(33)
    print test_stack
    test_stack.pop()
    test_stack.pop()
    print test_stack
    print test_stack.top()
    print test_stack.empty()

