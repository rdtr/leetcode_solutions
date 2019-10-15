class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if k == 0 or len(s) == 0:
            return 0

        table = {}
        maxlength = 0

        left, right = 0, 0

        while right < len(s):
            table[s[right]] = table[s[right]] + 1 if s[right] in table else 1
            if len(table) <= k:
                if right - left + 1 > maxlength:
                    maxlength = right - left + 1
                right += 1
                continue

            while len(table) > k and left < right:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del (table[s[left]])

                left += 1
            if len(table) <= k and right - left + 1 > maxlength:
                maxlength = right - left + 1
            right += 1
        return maxlength
