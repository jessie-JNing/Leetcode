#!/usr/bin/env python
# encoding: utf-8

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.


@author: Jessie

@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_m = (C-A)*(D-B)
        area_n = (G-E)*(H-F)

        delta_x = self.overlap(A, C, E, G)
        delta_y = self.overlap(B, D, F, H)

        return (area_m + area_n) - (delta_x * delta_y)


    def overlap(self, aa, bb, cc, dd):
        if cc < aa:
            if dd < aa:
                return 0
            elif dd < bb:
                return dd - aa
            else:
                return bb - aa

        elif cc < bb:
            if dd < bb:
                return dd - cc
            else:
                return bb - cc
        else:
            return 0




if __name__=="__main__":
    A = 0
    B = 0
    C = 0
    D = 0
    E = -1
    F = -1
    G = 1
    H = 1




    test = Solution()
    print test.computeArea(A,B,C,D,E,F,G,H)