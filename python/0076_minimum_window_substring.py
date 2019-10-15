from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        m = defaultdict(int)
        a = defaultdict(int)

        for ch in t:
            m[ch] += 1
        counter = len(m)

        left, right = 0, 0

        res, resLen = "", 0
        while right < len(s):
            ch = s[right]
            right += 1

            if ch in m:
                a[ch] += 1

                if a[ch] == m[ch]:
                    counter -= 1
                if counter == 0:
                    res = s[left:right]
                    resLen = right - left
                    break

        while True:
            while left < len(s):
                ch = s[left]
                left += 1

                if ch in m:
                    a[ch] -= 1
                    if a[ch] < m[ch]:
                        counter += 1
                        break

                if counter == 0 and resLen >= right - left:
                    resLen = right - left
                    res = s[left:right]

            if left == len(s):
                break

            while right < len(s):
                ch = s[right]
                right += 1

                if ch in m:
                    a[ch] += 1

                    if a[ch] == m[ch]:
                        counter -= 1
                    if counter == 0:
                        if resLen >= right - left:
                            res = s[left:right]
                            resLen = right - left
                        break

        return res
