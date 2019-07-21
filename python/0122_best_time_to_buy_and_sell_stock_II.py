class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        i = 0
        localmin, localmax = 0, 0
        while i < len(prices):
            while i < len(prices):
                localmin = i
                if i < len(prices) - 1 and prices[i + 1] > prices[i]:
                    i += 1
                    break
                i += 1

            while i < len(prices):
                localmax = i
                if i < len(prices) - 1 and prices[i + 1] < prices[i]:
                    i += 1
                    break
                i += 1

            if localmin < localmax:
                res += prices[localmax] - prices[localmin]
        return res