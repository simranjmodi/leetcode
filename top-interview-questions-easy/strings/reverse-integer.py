"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        if x < 0:
            sign = 1
            x = abs(x)
        else:
            sign = 0

        def getMaxDigit(x):
            return int(log(x) / log(10)) + 1

        div = 10 ** (getMaxDigit(x) - 1)
        new_int = 0
        factor = 1

        print(div)
        while x > 0:
            digit = x // div
            x -= digit * div

            new_int += digit * factor

            div /= 10
            factor *= 10

        def inRange(new_int):
            if new_int < -2 ** 31:
                return False
            if new_int > 2 ** 31 - 1:
                return False
            return True

        if sign and inRange(new_int):
            return -int(new_int)
        elif inRange(new_int):
            return int(new_int)
        else:
            return 0