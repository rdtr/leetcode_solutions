class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            if len(prev) == 1:
                res.append([1, 1])
                continue

            new = [1]
            j = 0
            while j + 1 < len(prev):
                new.append(prev[j] + prev[j + 1])
                j += 1
            new.append(1)
            res.append(new)
        return res