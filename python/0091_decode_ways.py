class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        slen = len(s)
        if slen == 0:
            return 0

        dp = [0] * slen
        for i, ch in enumerate(s):
            if i == 0:
                dp[0] = 1 if '1' <= s[i] and s[i] <= '9' else 0
                continue

            if i == 1:
                if self.isValid(s[:2]):
                    dp[1] = 2 if '1' <= s[1] and s[1] <= '9' else 1
                elif '1' <= s[1] and s[1] <= '9':
                    dp[1] = dp[0]
                continue

            if self.isValid(s[i - 1:i + 1]):
                dp[i] = dp[i - 2] + dp[i - 1] if '1' <= s[i] and s[i] <= '9' else dp[i - 2]
            elif '1' <= s[i] and s[i] <= '9':
                dp[i] = dp[i - 1]
        return dp[-1]

    def isValid(self, s):
        return '10' <= s and s <= '26'
