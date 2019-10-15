class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        mlen = len(matrix)
        if mlen == 0:
            return 0
        nlen = len(matrix[0])
        if nlen == 0:
            return 0
        
        heights = [[0 for x in range(nlen)] for y in range(mlen + 1)]
        for m in range(mlen):
            for n in range(nlen):
                if matrix[m][n] == '1':
                    heights[m][n] = heights[m][n-1] + 1 if n > 0 else 1 

        res = 0
        for n in range(nlen):
            stack = []
            for m in range(len(heights)):
                while stack and heights[stack[-1]][n] >= heights[m][n]:
                    prev = stack.pop(-1)
                    height = heights[prev][n]
                    width = m - stack[-1] - 1 if stack else m
                    
                    res = max(res, height * width)
                stack.append(m)

        return res