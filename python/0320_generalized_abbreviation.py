from collections import deque


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.helper(word, 0, 0, '', res)
        return res

    def helper(self, word, pos, length, cur, res):
        if pos >= len(word):
            if length > 0:
                cur += str(length)
            res.append(cur)
            return

        if length == 0:  # just consume one character
            self.helper(word, pos + 1, 0, cur + word[pos], res)
        else:  # perform abbr
            self.helper(word, pos + 1, 0, cur + str(length) + word[pos], res)
        # skip this character and increment abbr length
        self.helper(word, pos + 1, length + 1, cur, res)

