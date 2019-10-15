class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbrMap = {}
        self.wordSet = set()
        for word in dictionary:
            if word in self.wordSet:
                continue
            self.wordSet.add(word)

            abbr = self.getAbbr(word)
            if abbr not in self.abbrMap:
                self.abbrMap[abbr] = 1
            else:
                self.abbrMap[abbr] += 1

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.getAbbr(word)
        return abbr not in self.abbrMap or (self.abbrMap[abbr] == 1 and word in self.wordSet)

    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]
