#!/usr/bin/env python
# encoding: utf-8

"""

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

In this problem, we are asked to divide two integers.
However, we are not allowed to use division, multiplication and mod operations.
So, what else can we use? Yeah, bit manipulations.

Let's do an example and see how bit manipulations work.
Suppose we want to divide 15 by 3, so 15 is dividend and 3 is divisor.
Well, division simply requires us to find how many times we can subtract the
divisor from the the dividend without making the dividend negative.

Let's get started. We subtract 3 from 15 and we get 12, which is positive.
Let's try to subtract more. Well, we shift 3 to the left by 1 bit and we get 6.
Subtracting 6 from 15 still gives a positive result.
Well, we shift again and get 12. We subtract 12 from 15 and it is still positive.
We shift again, obtaining 24 and we know we can at most subtract 12.
Well, since 12 is obtained by shifting 3 to left twice, we know it is 4 times of 3.
How do we obtain this 4? Well, we start from 1 and shift it to left twice at the same time.
We add 4 to an answer (initialized to be 0). In fact, the above process is like 15 = 3 * 4 + 3.
We now get part of the quotient (4), with a remainder 3.

Then we repeat the above process again. We subtract divisor = 3 from the remaining
dividend = 3 and obtain 0. We know we are done. No shift happens, so we simply add 1 << 0 to the answer.

Now we have the full algorithm to perform division.
According to the problem statement, we need to handle some exceptions, such as overflow.
Well, two cases may cause overflow:
- divisor = 0;
- dividend = INT_MIN (-2147483648) and divisor = -1 (because abs(INT_MIN) = INT_MAX + 1).

@author: Jessie

@email: jessie.JNing@gmail.com
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return "MAX_INT"

        elif (dividend<=-2147483648 and divisor == -1):
            return 2147483648

        else:
            x = dividend if dividend >= 0 else -dividend
            y = divisor if divisor >= 0 else -divisor
            result = 0
            while x>=y:
                x = x - y
                result += 1
            if (dividend>=0 and divisor>0) or (dividend<=0 and divisor<0):
                return result
            else:
                return -result-1

    def divide_2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return "MAX_INT"

        elif (dividend<=-2147483648 and divisor == -1):
            return 2147483648

        else:
            positive = (dividend < 0) is (divisor < 0)   # calculate XOR
            dividend, divisor = abs(dividend), abs(divisor)
            res = 0
            while dividend >= divisor:
                temp, i = divisor, 1
                while dividend >= temp:
                    dividend -= temp
                    res += i
                    i <<= 1
                    temp <<= 1
            if not positive:
                res = -res
            return res

if __name__=="__main__":

    solution_obj = Solution()
    #print solution_obj.divide_2(-2147483648, -1)
    for k in range(100):
        print k/-10, solution_obj.divide_2(k, -10)
