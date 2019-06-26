class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x

        res = 0
        while x > 0:
            rem = x % 10
            x = x // 10

            res += rem
            if x > 0:
                res *= 10
        res *= flag
        if 2 ** 31 - 1 >= res >= -1 * 2 ** 31:
            return res
        return 0