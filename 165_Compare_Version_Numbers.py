#!/usr/bin/env python
# encoding: utf-8

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
        print v1, v2   #  [1] [1, 1]
        d = len(v2) - len(v1)
        print v1 + [0]*d, v2 + [0]*-d  # [1, 0] [1, 1]
        return cmp(v1 + [0]*d, v2 + [0]*-d)


    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = self.helper(version1), self.helper(version2)
        return 1 if v1 > v2 else (-1 if v1 < v2 else 0)

    def helper(self, v):
        v = map(int, v.split("."))
        # tackle tailing 0 case: 1.0.0 vs 1
        i = len(v)-1
        while i >= 0 and v[i] == 0:
            i -= 1
        return v[:i+1]

    def compareVersion3(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split('.')
        s2 = version2.split('.')
        # Ailgning them
        if len(s1) >= len(s2):
            s2.extend('0'*(len(s1)-len(s2)))
        else:
            s1.extend('0'*(len(s2)-len(s1)))

        c = [int(s1[i])-int(s2[i]) for i in range(len(s1))]
        for item in c:
            if item < 0:
                return -1
            elif item > 0:
                return 1
        return 0

    def compareVersion4(self, version1, version2):
        from itertools import izip_longest
        v1 = (int(n) for n in version1.split('.'))
        v2 = (int(n) for n in version2.split('.'))

        for n1, n2 in izip_longest(v1, v2, fillvalue=0):
            print n1, n2
            if n1> n2:
                return 1
            elif n1< n2:
                return -1
        return 0



if __name__=="__main__":
    test = Solution()
    print test.compareVersion4("1",  "1.1")