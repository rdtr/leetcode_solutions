class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        dist, left, right = 0, 0, 0
        for i, ch in enumerate(s):
            if ch == '(':
                right += 1
            else:
                left += 1

            dist += 1
            if right == left:
                res = max(dist, res)
            elif right < left:
                dist, left, right = 0, 0, 0

        dist, left, right = 0, 0, 0
        for i, ch in enumerate(s[::-1]):
            if ch == '(':
                right += 1
            else:
                left += 1

            dist += 1
            if right == left:
                res = max(dist, res)
            elif right > left:
                dist, left, right = 0, 0, 0

        return res
