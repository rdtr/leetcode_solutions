class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = [0] * len(prices)
        for i, p in enumerate(prices):
            if i == 0:
                minSoFar[i] = p
            else:
                minSoFar[i] = min(minSoFar[i - 1], p)

        res = 0
        for i, p in enumerate(prices):
            res = max(p - minSoFar[i], res)
        return res