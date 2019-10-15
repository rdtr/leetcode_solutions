class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        res = [1, 1]
        i = 1

        while i < rowIndex:
            new = [1]
            for j in range(len(res) - 1):
                new.append(res[j] + res[j + 1])
            new.append(1)
            res = new
            i += 1
        return res