"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # n=5
        def climbStairsAux(n, steps):
            print(n, steps)
            if n <= 3:
                return n
            elif n < len(steps):
                return steps[n]
            else:
                steps.append(climbStairsAux(n - 1, steps) + climbStairsAux(n - 2, steps))
                print(steps)
                return steps[n]

        steps = [0, 1, 2, 3]
        return climbStairsAux(n, steps)
