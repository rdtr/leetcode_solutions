class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSoFar = 0
        res = ''
        DP = [[0 for x in range(len(s))] for x in range(len(s))]
        for i in range(len(s)):
            DP[i][i] = True

            if maxSoFar < 1:
                res = s[i]
                maxSoFar = 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                DP[i][i + 1] = True
                if maxSoFar < 2:
                    res = s[i:i + 2]
                    maxSoFar = 2

        for width in range(3, len(s) + 1):
            for left in range(len(s)):
                right = left + width - 1
                if right >= len(s):
                    break
                if DP[left + 1][right - 1] and s[left] == s[right]:
                    DP[left][right] = True
                    if right - left + 1 > maxSoFar:
                        maxSoFar = right - left + 1
                        res = s[left:right + 1]
        return res