"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        def wrapper(n):
            if n == 1:  # base case
                return "1"
            # else
            previous_count = wrapper(n - 1)
            result = []
            j=0
            while j < len(previous_count):
                current_count = 0
                while j < len(previous_count) - 1 and previous_count[j] == previous_count[j + 1]:
                    current_count += 1
                    j += 1
                #if j == len(previous_count) - 1:

                result.append(str(current_count + 1))
                result.append(str(previous_count[j]))
                j += 1
            print(result)
            return result

        return "".join(wrapper(n))