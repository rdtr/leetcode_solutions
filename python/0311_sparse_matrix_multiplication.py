class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        x = len(A)
        y, z = 0, 0
        if x != 0:
            y = len(A[0])
        if len(B) != 0:
            z = len(B[0])

        res = [[0] * z for i in range(x)]
        for i in range(x):
            for j in range(y):
                if A[i][j] != 0:
                    for k in range(z):
                        res[i][k] += A[i][j] * B[j][k]
        return res
