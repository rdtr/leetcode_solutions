class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        mid = low + (high - low) // 2

        while True:
            p = mid ** 2
            if p == x:
                return mid
            elif p < x:
                low = mid
            else:
                high = mid - 1
            mid = low + (high - low) // 2

            if high - 1 == low:
                if high ** 2 <= x:
                    return high
                return low
            elif high == low:
                return low
