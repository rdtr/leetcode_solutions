class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        slen, elen = len(start), len(end)
        if slen != elen:
            return False

        p1, p2 = 0, 0

        while True:
            while p1 < slen and start[p1] == 'X':
                p1 += 1
            while p2 < elen and end[p2] == 'X':
                p2 += 1

            if (p1 == slen and p2 != elen) or (p1 != slen and p2 == elen):
                return False
            elif p1 == slen and p2 == elen:
                return True

            if start[p1] != end[p2]:
                return False
            elif (start[p1] == 'R' and p1 > p2) or (start[p1] == 'L' and p1 < p2):
                return False

            p1 += 1
            p2 += 1
