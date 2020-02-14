class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        count = 0
        res = []
        
        i = len(S) - 1
        while i >= 0:
            if count == K:
                if S[i] == '-':
                    res.append(S[i])
                else:
                    res.append('-')
                count = 0
                continue
            else:
                if S[i] == '-':
                    i -= 1
                else:
                    res.append(S[i].upper())
                    i -= 1
                    count += 1
        if res and res[-1] == '-':
            res = res[:-1]
        res.reverse()
        return ''.join(res)