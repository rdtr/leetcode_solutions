class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        slen, tlen = len(s), len(t)
        dp = [[0 for x in range(tlen+1)] for y in range(slen+1)]
        for S in range(slen+1):
            dp[S][0] = 1
        
        for T in range(tlen):
            for S in range(slen):
                if t[T] == s[S]:
                    dp[S+1][T+1] = dp[S][T] + dp[S][T+1]        
                else:
                    dp[S+1][T+1]= dp[S][T+1]
        return dp[-1][-1]
                    