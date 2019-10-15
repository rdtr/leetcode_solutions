from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        mp = defaultdict(lambda: 0)
        res = 0

        left, right = 0, 0
        while len(mp) <= 2 and right <= len(s) - 1:
            mp[s[right]] += 1
            if len(mp) <= 2 and right - left + 1 > res:
                res = right - left + 1
            right += 1

        while right <= len(s) - 1:
            while len(mp) >= 3:
                mp[s[left]] -= 1
                if mp[s[left]] == 0:
                    mp.pop(s[left], None)
                left += 1

            while len(mp) <= 2 and right <= len(s) - 1:
                mp[s[right]] += 1
                if len(mp) <= 2 and right - left + 1 > res:
                    res = right - left + 1
                right += 1
        return res
