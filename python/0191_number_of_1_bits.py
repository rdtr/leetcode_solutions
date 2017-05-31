class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        i = 0
        while True:
            i += 1
            n = n & (n - 1)
            if n == 0:
                break
        return i