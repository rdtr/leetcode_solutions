class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = pos2 = -1
        res = float('+inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1:
                res = min(res, abs(pos1 - pos2))
        return res