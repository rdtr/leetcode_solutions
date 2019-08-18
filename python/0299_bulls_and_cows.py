class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        smap, gmap = {}, {}
        for i, ch in enumerate(secret):
            if ch in smap:
                smap[ch][i] = True
            else:
                smap[ch] = {i: True}

        a = b = 0
        exactFound = set()
        for i, ch in enumerate(guess):
            if ch in smap and i in smap[ch]:
                a += 1
                del smap[ch][i]
                exactFound.add(i)

        for i, ch in enumerate(guess):
            if i not in exactFound and ch in smap and len(smap[ch]) > 0:
                b += 1
                k = None
                for key in smap[ch].keys():
                    k = key
                    break
                del smap[ch][k]

        return str(a) + 'A' + str(b) + 'B'
