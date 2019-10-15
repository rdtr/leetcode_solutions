class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        l1, l2 = len(word1), len(word2)
        if l1 == 0: return l2

        DP = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                    continue
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

        lcs = DP[-1][-1]
        return l1 - lcs + l2 - lcs


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        l1, l2 = len(word1), len(word2)
        if l1 == 0: return l2

        DP = [0 for _ in range(l2 + 1)]
        for i in range(1, l1 + 1):
            newDP = [0 for _ in range(l2 + 1)]
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    newDP[j] = DP[j - 1] + 1
                else:
                    newDP[j] = max(DP[j], newDP[j - 1])
            DP = newDP

        lcs = DP[-1]
        return l1 - lcs + l2 - lcs