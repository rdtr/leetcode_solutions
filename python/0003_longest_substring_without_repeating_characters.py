class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = 0
        l = 0
        m = {}
        for i, ch in enumerate(s):
            if ch in m and m[ch] >= st:
                st = m[ch] + 1
                m[ch] = i
                continue

            dist = i - st + 1
            if l < dist:
                l = dist
            m[ch] = i
        return l


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        m = defaultdict(lambda: 0)
        l = r = 0

        maxSoFar = 0
        while True:
            while r < len(s) and m[s[r]] == 0:
                m[s[r]] = 1
                maxSoFar = max(maxSoFar, r - l + 1)
                r += 1

            if r >= len(s) - 1:
                break

            while l < len(s) and s[l] != s[r]:
                m[s[l]] -= 1
                l += 1
            m[s[l]] -= 1
            l += 1
        return maxSoFar
