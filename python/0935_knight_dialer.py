class Solution:
    def knightDialer(self, N: int) -> int:
        cur = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        i = 0
        m = 10 ** 9 + 7
        while i < N - 1:
            new = [0] * 10
            new[0] = (cur[4] + cur[6]) % m
            new[1] = (cur[6] + cur[8]) % m
            new[2] = (cur[7] + cur[9]) % m
            new[3] = (cur[4] + cur[8]) % m
            new[4] = (cur[0] + cur[3] + cur[9]) % m
            new[5] = 0
            new[6] = (cur[0] + cur[1] + cur[7]) % m
            new[7] = (cur[2] + cur[6]) % m
            new[8] = (cur[1] + cur[3]) % m
            new[9] = (cur[2] + cur[4]) % m
            cur = new
            i += 1
        return sum(cur) % m
