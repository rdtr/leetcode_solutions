class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        mlen = len(matrix)
        nlen = len(matrix[0])

        for m in range(mlen):
            for n in range(1, nlen):
                matrix[m][n] += matrix[m][n-1]

        res = 0
        for n0 in range(nlen):
            for n1 in range(n0, nlen):
                sumMap = {0: 1}
                cur = 0
                for m in range(mlen):
                    cur += matrix[m][n1] - (matrix[m][n0-1] if n0 > 0 else 0)
                    if cur - target in sumMap:
                        res += sumMap[cur - target]

                    if cur in sumMap:
                        sumMap[cur] += 1
                    else:
                        sumMap[cur] = 1
        return res
