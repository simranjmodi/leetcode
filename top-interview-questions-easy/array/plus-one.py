"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits):
        def func(digits):
            i = -1

            if len(digits) == 0:
                return [1]

            if digits[i] == 9:
                digits[i] = 0
                carry = func(digits[:i])
                digits = carry + digits[i:]
            else:
                digits[i] += 1

            return digits

        return func(digits)

