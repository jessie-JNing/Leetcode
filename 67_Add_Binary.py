#!/usr/bin/env python
# encoding: utf-8

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

@author: Jessie

@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aa = int(a, 2)
        bb = int(b, 2)
        return bin(aa + bb)[2:]

    def addBinary2(self, a, b):
        delta = len(a)-len(b)
        if delta > 0:
            b = '0'*delta + b
        elif delta < 0:
            a = '0'*(-delta) + a

        carrier = 0
        c = ''
        for i in range(len(a)-1, -1, -1):
            print a[i], b[i]
            if carrier == 0:
                if a[i] == b[i]:
                    if a[i]=='1':
                        carrier = 1
                    c +='0'
                else:
                    c += '1'

            else:
                if a[i] == b[i]:
                    if a[i]=='1':
                        carrier = 1
                        c += '1'
                    else:
                        c += '1'
                        carrier = 0
                else:
                    c += '0'
                    carrier = 1

        if carrier == 1:
            return '1' + ''.join([c[i] for i in range(len(c)-1,-1,-1)])
        else:
            return ''.join([c[i] for i in range(len(c)-1,-1,-1)])





if __name__=="__main__":

    test = Solution()
    print test.addBinary2('1010', '1011')