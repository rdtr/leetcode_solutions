class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False

        ht1 = [0] * 26
        ht2 = [0] * 26
        for ch in s1:
            ht1[ord(ch) - ord('a')] += 1

        left = right = 0
        while right < len(s2):
            while right < len(s2) and not self.covered(ht1, ht2):
                ht2[ord(s2[right]) - ord('a')] += 1
                right += 1

            while left < right and self.covered(ht1, ht2):
                if self.equal(ht1, ht2):
                    return True
                ht2[ord(s2[left]) - ord('a')] -= 1
                left += 1
        return False

    def covered(self, ht1, ht2):
        for c1, c2 in zip(ht1, ht2):
            if c1 > 0 and c2 < c1:
                return False
        return True

    def equal(self, ht1, ht2):
        for c1, c2 in zip(ht1, ht2):
            if c1 != c2:
                return False
        return True