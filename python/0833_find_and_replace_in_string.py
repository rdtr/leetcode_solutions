class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        replaces = [(x, y, z) for (x, y, z) in zip(indexes, sources, targets)]
        replaces.sort(key=lambda x: x[0])

        if not replaces:
            return S

        slen = len(S)
        if slen == 0:
            return S

        res = []
        c = 0
        i = 0
        while c < slen:
            if i >= len(replaces) or c < replaces[i][0]:
                res.append(S[c])
                c += 1
                continue

            source, target = replaces[i][1], replaces[i][2]
            if c + len(source) <= slen and S[c:c+len(source)] == source:
                res.extend([t for t in target])
                c += len(source)
            i += 1
        return ''.join(res)
