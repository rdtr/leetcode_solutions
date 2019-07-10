class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        mlen = len(matrix)
        if mlen == 0:
            return None

        left, right, top, bottom = 0, mlen - 1, 0, mlen - 1
        while left < right:
            for i in range(right - left):
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            left += 1
            right -= 1
            top += 1
            bottom -= 1