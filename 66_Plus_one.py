#!/usr/bin/env python
# encoding: utf-8

"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

@author: Jessie
@email: jessie.JNing@gmail.com
"""

class Solution(object):
    def plusOne(self, digits):
        i, plus_one = len(digits)-2, 0
        plus_one, new_dig = divmod(digits[len(digits)-1] + plus_one + 1, 10)
        digits[len(digits)-1] = new_dig

        while i>=0 and plus_one==1:
            plus_one, new_dig = divmod(digits[i] + plus_one, 10)
            digits[i] = new_dig
            i -= 1
        if plus_one ==1:
            digits.insert(0,1)
        return digits

    def plusOne_2(self, digits):
        i, plus_one = len(digits)-1, 1
        while i>=0 and plus_one==1:
            new_dig = (digits[i] + plus_one)/10
            plus_one = (digits[i] + plus_one)%10
            digits[i] = new_dig
            i-=1

        if plus_one ==1:
            digits.insert(0,1)
        return digits

    def plusOne_3(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i] +=1
                return digits
        digits.insert(0,1)
        return digits





if __name__=="__main__":
    nums_list = [2,1,2]
    nums_list= [9,9, 8]
    Solution_obj = Solution()

    print Solution_obj.plusOne_3(nums_list)