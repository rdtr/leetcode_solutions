class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                right = mid - 1
            else:
                left = mid + 1
