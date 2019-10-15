class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        chs = [x for x in dominoes]

        lefts, rights = [], []
        for i, domino in enumerate(chs):
            if domino == 'L':
                lefts.append(i)
            elif domino == 'R':
                rights.append(i)

        while lefts or rights:
            newLefts = []
            for i in lefts:
                if i == 0 or chs[i - 1] == 'R' or chs[i - 1] == 'L' or (
                        i > 1 and chs[i - 2] == 'R'):
                    continue
                newLefts.append(i - 1)

            newRights = []
            for i in rights:
                if i == len(chs) - 1 or chs[i + 1] == 'R' or chs[
                        i + 1] == 'L' or (i < len(chs) - 2
                                          and chs[i + 2] == 'L'):
                    continue
                newRights.append(i + 1)

            for newLeft in newLefts:
                chs[newLeft] = 'L'
            for newRight in newRights:
                chs[newRight] = 'R'

            lefts, rights = newLefts, newRights
        return ''.join(chs)