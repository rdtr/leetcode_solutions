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

        curm = mlen - 1
        curn = 0

        while curn < nlen and curm >= 0:
            val = matrix[curm][curn]
            if val == target:
                return True
            elif target < val:
                curm -= 1
            else:
                curn += 1
        return False
