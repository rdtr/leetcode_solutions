class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i1, i2 = 0, 0
            while i1 < len(S) and i2 < len(word):
                if S[i1] == word[i2]:
                    cnt2 = 1
                    for i in range(i2 + 1, len(word)):
                        if word[i] != word[i2]:
                            break
                        cnt2 += 1

                    cnt1 = 1
                    for i in range(i1 + 1, len(S)):
                        if S[i] != S[i1]:
                            break
                        cnt1 += 1

                    if cnt1 == cnt2 or (cnt1 > cnt2 and cnt1 >= 3):
                        i1 += cnt1
                        i2 += cnt2
                        continue
                    break
                break
            if i1 == len(S) and i2 == len(word):
                res += 1
        return res