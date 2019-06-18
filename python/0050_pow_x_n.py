class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n == 0:
            return 1
        elif n < 0:
            neg = True
            n = -n

        a, b = 1, n
        while b > 0:
            if b % 2 == 1:
                a *= x
                b -= 1
            else:
                x = x * x
                b = b >> 1

        return a if not neg else 1 / a