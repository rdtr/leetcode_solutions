class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """

        wlen = len(words)
        if wlen == 0:
            return []
        elif wlen == 1:
            return [[words[0]]]

        num = len(words[0])
        m = self.buildMap(words)

        res = []
        curWords = []
        for i in range(wlen):
            curWords.append(words[i])
            self.populatePerm(words, num, curWords, res, m)
            curWords.pop()
        return res

    def populatePerm(self, words, num, curWords, res, mp):
        if len(curWords) == num:
            res.append(curWords.copy())
            return

        depth = len(curWords)
        prefix = ''
        for i in range(depth):
            prefix += curWords[i][depth]

        if prefix not in mp:
            return
        nexts = mp[prefix]

        for n in nexts:
            curWords.append(n)
            self.populatePerm(words, num, curWords, res, mp)
            curWords.pop()

    def buildMap(self, words):
        m = {}
        for word in words:
            for i in range(1, len(word)):
                if word[:i] in m:
                    m[word[:i]].append(word)
                else:
                    m[word[:i]] = [word]
        return m
