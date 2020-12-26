class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        num = len(cardPoints)
        if num <= k:
            return sum(cardPoints)

        res = cur = sum(cardPoints[:k])
        left = k - 1
        right = num - 1

        while left >= 0:
            cur = cur - cardPoints[left] + cardPoints[right]
            res = max(cur, res)

            left -= 1
            right -= 1
        return res