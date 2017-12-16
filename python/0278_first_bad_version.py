class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n - 1

        while True:
            m = l + (r - l) / 2
            if isBadVersion(m + 1):
                r = m
            else:
                l = m + 1

            if r - l == 1:
                if isBadVersion(l + 1):
                    return l + 1
                return r + 1
            elif l >= r:
                break
        return r + 1
