"""
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # s = "LVIII"
        if len(s) == 1:
            return mapping[s[0]]

        number = 0

        i = 1
        while i < len(s):
            current_char = s[i - 1]
            next_char = s[i]
            print(current_char, next_char)
            print(i)
            if mapping[current_char] < mapping[next_char]:
                number += mapping[next_char] - mapping[current_char]
                i += 2
            else:
                number += mapping[current_char]
                i += 1
            print(number)

        if mapping[s[-1]] <= mapping[s[-2]]:
            final_char = s[-1]
            number += mapping[s[-1]]
        return number
