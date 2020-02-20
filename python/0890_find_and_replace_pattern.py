class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue

            m = {}
            mapped = set()
            add = True
            for i in range(len(word)):
                wch = word[i]
                pch = pattern[i]

                if wch in m:
                    if m[wch] == pch:
                        continue
                    else:
                        add = False
                        break
                elif pch in mapped:
                    add = False
                    break
                else:
                    m[wch] = pch
                    mapped.add(pch)

            if add:
                res.append(word)
        return res
