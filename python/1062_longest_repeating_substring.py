from collections import deque


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        slen = len(S)
        DP = [[0 for x in range(slen)] for y in range(slen)]

        for i in range(1, slen):
            if S[i] == S[0]:
                DP[0][i] = 1

        res = 0
        for i in range(1, slen):
            for j in range(i + 1, slen):
                if S[i] == S[j]:
                    DP[i][j] = DP[i-1][j-1] + 1
                    res = max(res, DP[i][j])
        return res
