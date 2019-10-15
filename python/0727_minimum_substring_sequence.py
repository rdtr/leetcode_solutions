class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        if len(T) == 1:
            if S.find(T) != -1:
                return T
            return ''

        dp = [[-1 for x in range(len(T))] for y in range(len(S))]

        if S[0] == T[0]:
            dp[0][0] = 0

        res, resLen = '', -1
        for i in range(1, len(S)):
            for j in range(len(T)):
                if S[i] == T[j]:
                    if j == 0:
                        dp[i][j] = i
                    elif dp[i - 1][j - 1] != -1:
                        dp[i][j] = dp[i - 1][j - 1]
                        if j == len(T) - 1:
                            newLen = i - dp[i][j] + 1
                            if resLen == -1 or resLen > newLen:
                                res, resLen = S[dp[i][j]: i + 1], newLen
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return res
