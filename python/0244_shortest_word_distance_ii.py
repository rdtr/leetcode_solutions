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
        return refrom collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.cache = {}
        self.posDict = defaultdict(lambda: [])

        for i, word in enumerate(wordsDict):
            self.posDict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]
        elif (word2, word1) in self.cache:
            return self.cache[(word2, word1)]

        posList1 = self.posDict[word1]
        posList2 = self.posDict[word2]
        i1, i2 = 0, 0

        minDistance = float('+inf')
        while i1 < len(posList1) and i2 < len(posList2):
            pos1 = posList1[i1]
            pos2 = posList2[i2]
            minDistance = min(abs(pos1 - pos2), minDistance)

            if pos1 <= pos2:
                i1 += 1
            else:
                i2 += 1

        self.cache[(word1, word2)] = minDistance
        return minDistance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)s