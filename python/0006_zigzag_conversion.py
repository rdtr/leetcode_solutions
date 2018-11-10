class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        res, rowNum = [], 0
        jump1, jump2 = numRows * 2 - 4, 2
        while rowNum < numRows:
            if rowNum == 0 or rowNum == numRows - 1:
                i = rowNum
                while i < len(s):
                    res.append(s[i])
                    i += numRows * 2 - 2
                rowNum += 1
                continue

            i, curJump = rowNum, jump1
            while i < len(s):
                res.append(s[i])
                i += curJump
                curJump = jump2 if curJump == jump1 else jump1
            rowNum, jump1, jump2 = rowNum + 1, jump1 - 2, jump2 + 2
        return ''.join(res)


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        rows = [[] for x in range(numRows)]

        i = 0
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break
                rows[j].append(s[i])
                i += 1
            for j in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                rows[j].append(s[i])
                i += 1

        return ''.join([''.join(row) for row in rows])
