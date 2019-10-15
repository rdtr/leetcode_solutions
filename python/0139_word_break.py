class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for word in wordDict:
            if len(word) <= len(s) and s[:len(word)] == word:
                dp[len(word) - 1] = True
        
        for i in range(len(dp)):
            if dp[i]:
                for word in wordDict:
                    if i + len(word) < len(s) and s[i+1:i+len(word)+1] == word:
                        dp[i+len(word)] = True
        return dp[-1]