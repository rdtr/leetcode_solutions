class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1

        v = 1
        while True:
            for i in range(left, right + 1):
                matrix[top][i] = v
                v += 1
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                matrix[i][right] = v
                v += 1
            right -= 1
            if left > right:
                break

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = v
                v += 1
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = v
                v += 1
            left += 1
            if left > right:
                break
        return matrix