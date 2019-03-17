class Solution:
    DIGITS = [
        [],
        [],
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l'],
        ['m', 'n', 'o'],
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v'],
        ['w', 'x', 'y', 'z']
    ]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == '':
            return []
        return self.doLetterCombinations(digits, 0)

    def doLetterCombinations(self, digits, i):
        digit = int(digits[i])
        cands = Solution.DIGITS[digit]

        if i == len(digits) - 1:
            return cands

        suffixList = self.doLetterCombinations(digits, i + 1)

        res = []
        for cand in cands:
            for suffix in suffixList:
                res.append(cand + suffix)
        return res
