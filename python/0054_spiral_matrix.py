class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        mlen = len(matrix)
        if mlen == 0:
            return []
        nlen = len(matrix[0])
        if nlen == 0:
            return []

        left, right, top, bottom = 0, nlen, 0, mlen
        res = []
        while True:
            for n in range(left, right):
                res.append(matrix[top][n])

            top += 1
            if top >= bottom:
                break

            for m in range(top, bottom):
                res.append(matrix[m][right - 1])

            right -= 1
            if right <= left:
                break

            for n in reversed(range(left, right)):
                res.append(matrix[bottom - 1][n])

            bottom -= 1
            if bottom <= top:
                break

            for m in reversed(range(top, bottom)):
                res.append(matrix[m][left])

            left += 1
            if left >= right:
                break
        return res