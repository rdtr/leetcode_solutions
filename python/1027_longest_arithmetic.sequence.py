from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        DP = [defaultdict(lambda: 0) for _ in range(len(A))]

        res = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                DP[j][diff] = max(DP[j][diff], DP[i][diff] + 1, 1)
                res = max(DP[j][diff], res)
        return res + 1