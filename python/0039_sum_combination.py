class Solution:
    def combinationSum(self, candidates, target):
        dp = [[] for x in range(target+1)]
        for candidate in candidates:
            if candidate <= target:
                dp[candidate].append([candidate])
 
        for i, iSumsList in enumerate(dp):
            for candidate in candidates:
                if i + candidate > target:
                    continue
                    
                for iSums in iSumsList:
                    if iSums[-1] <= candidate:
                        dp[i+candidate].append(iSums + [candidate])
        return dp[target]
        