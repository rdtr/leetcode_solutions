class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if not s1 and s2:
            return s2 == s3
        elif s1 and not s2:
            return s1 == s3
        elif not s1 and not s2:
            return not s3

        DP = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        if s1[0] == s3[0]:
            DP[1][0] = 0
        if s2[0] == s3[0]:
            DP[0][1] = 0

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if DP[i][j] >= 0 and DP[i][j] < l3 - 1:
                    prev = DP[i][j]
                    if i < l1 and s3[prev + 1] == s1[i]:
                        DP[i + 1][j] = prev + 1
                    if j < l2 and s3[prev + 1] == s2[j]:
                        DP[i][j + 1] = prev + 1
        return DP[-1][-1] == l3 - 1
