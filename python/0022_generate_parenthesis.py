class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        self.helper(res, [], n, n)
        return res

    def helper(self, res, cur, leftNum, rightNum):
        if leftNum == 0 and rightNum == 0:
            res.append(''.join(cur))
            return

        if leftNum > 0:
            cur.append('(')
            self.helper(res, cur, leftNum - 1, rightNum)
            cur.pop()
        if rightNum > leftNum:
            cur.append(')')
            self.helper(res, cur, leftNum, rightNum - 1)
            cur.pop()
