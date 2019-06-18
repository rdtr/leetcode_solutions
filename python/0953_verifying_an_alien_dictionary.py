class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = [0] * 26
        for i, ch in enumerate(order):
            orderMap[ord(ch) - ord('a')] = i

        prev = []
        for word in words:
            cur = [orderMap[ord(ch) - ord('a')] for ch in word]
            if prev:
                ok = False
                for i, c in enumerate(cur):
                    if i < len(prev):
                        if cur[i] > prev[i]:
                            ok = True
                            break
                        elif cur[i] < prev[i]:
                            return False
                if not ok:
                    return False
            prev = cur
        return True