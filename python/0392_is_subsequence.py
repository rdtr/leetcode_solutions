class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen, tlen = len(s), len(t)
        if slen == 0:
            return True

        sindex = 0
        for i in range(tlen):
            if t[i] == s[sindex]:
                sindex += 1
                if sindex >= slen:
                    return True
                continue
        return False
