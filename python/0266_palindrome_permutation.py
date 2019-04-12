from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = defaultdict(lambda: 0)
        for ch in s:
            m[ch] += 1

        oddNum = 0
        for _, val in m.items():
            if val % 2 == 1:
                oddNum += 1

        return oddNum == 0 or oddNum == 1