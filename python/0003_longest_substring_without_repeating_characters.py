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
