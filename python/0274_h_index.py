class Solution:
    def hIndex(self, citations: List[int]) -> int:
        clen = len(citations)
        if clen == 0:
            return 0

        citations.sort(reverse=True)
        i = 0
        while i < clen:
            if i + 1 <= citations[i]:
                i += 1
                continue
            break
        return i


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        clen = len(citations)
        if clen == 0:
            return 0

        buckets = [0] * (clen + 1)
        for c in citations:
            buckets[min(c, clen)] += 1

        i = len(buckets) - 1
        s = 0
        while i >= 0:
            s += buckets[i]
            if s >= i:
                break
            i -= 1
        return i
