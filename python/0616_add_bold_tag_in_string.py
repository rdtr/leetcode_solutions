class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        slen = len(s)
        if slen == 0:
            return s

        bolds = [False] * slen
        for i, _ in enumerate(s):
            word, ok = self.check(s, i, dict)
            if ok:
                for j in range(i, i + len(word)):
                    bolds[j] = True

        res = ''
        isBold = False

        for i, bold in enumerate(bolds):
            if bold:
                if not isBold:
                    isBold = True
                    res += '<b>'
                res += s[i]

                if i == slen - 1:
                    res += '</b>'
                continue

            if isBold:
                isBold = False
                res += '</b>'
            res += s[i]
        return res

    def check(self, s, i, dict):
        length = 0
        res = ''
        for word in dict:
            if i + len(word) - 1 >= len(s):
                continue
            if s[i:i + len(word)] == word:
                if len(word) > length:
                    length = len(word)
                    res = word

        if not res:
            return '', False
        return res, True
