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

class MinStack(object):
    def __init__(self):
        self.data = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        min_value = self.getMin()
        if not min_value or min_value > x:
            min_value = x
        self.data.append((x, min_value))
    # @return nothing
    def pop(self):
        if len(self.data)>0:
            self.data.pop()


    # @return an integer
    def top(self):
        if len(self.data)>0:
            return self.data[-1][0]

    # @return an integer
    def getMin(self):
        if len(self.data)>0:
            return self.data[-1][-1]
        else:
            return None



if __name__=="__main__":
    stack = MinStack()
    stack.push(3)
    print stack
    stack.push(5)
    print stack
    stack.push(2)
    print stack
    stack.push(1)
    print stack

    stack.pop()
    print stack
    stack.pop()
    print stack
    print stack.top()