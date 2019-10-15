class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        chs = [ch for ch in s]
        clen = len(chs)
        i = 0
        while i + k - 1 < clen:
            left, right = i, i + k - 1
            while left < right:
                chs[left], chs[right] = chs[right], chs[left]
                left += 1
                right -= 1
            i += 2 * k

        # handle the last characters with insufficient length (< k)
        left, right = i, clen - 1
        while left < right:
            chs[left], chs[right] = chs[right], chs[left]
            left += 1
            right -= 1
        return "".join(chs)
