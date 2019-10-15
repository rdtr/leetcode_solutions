class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        mlen = len(matrix)
        if mlen == 0:
            return False
        nlen = len(matrix[0])

        lo, hi = 0, mlen * nlen
        while lo < hi:
            mid = lo + (hi - lo) // 2

            row = mid // nlen
            col = mid % nlen
            val = matrix[row][col]

            if val == target:
                return True
            elif val <= target:
                lo = mid + 1
            else:
                hi = mid
        return False