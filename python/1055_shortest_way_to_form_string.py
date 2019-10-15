class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = i = 0
        while i < len(target):
            before = i

            j = 0
            while j < len(source) and i < len(target):
                if source[j] == target[i]:
                    i += 1
                j += 1

            if i == before:
                return -1
            res += 1

        return res