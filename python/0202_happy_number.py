class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)

            s = 0
            while n > 0:
                d = n % 10
                s += d * d
                n = n // 10
            if s == 1:
                return True
            n = s
