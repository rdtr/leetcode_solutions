class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        for index, source, target in sorted(zip(indexes, sources, targets), reverse=True):
            if S[index:index + len(source)] == source:
                S = S[:index] + target + S[index + len(source):]
        return S
