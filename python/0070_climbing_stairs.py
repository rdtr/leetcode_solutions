class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev0 = 2
        prev1 = 1
        cur = 0
        for i in range(3, n + 1):
            cur = prev0 + prev1
            prev0, prev1 = cur, prev0
        return cur
