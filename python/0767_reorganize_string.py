class Solution:
    def reorganizeString(self, S: str) -> str:
        mp = {}
        for ch in S:
            if ch not in mp:
                mp[ch] = 1
            else:
                mp[ch] += 1

        chs = []
        for k, v in mp.items():
            if v > (len(S) + 1) // 2:
                return ''
            chs.append((-v, k))

        heapq.heapify(chs)

        res = ''
        while len(chs) >= 2:
            cnt1, ch1 = heapq.heappop(chs)
            cnt2, ch2 = heapq.heappop(chs)

            res = res + ch1 + ch2

            if cnt1 < -1:
                heapq.heappush(chs, (cnt1 + 1, ch1))
            if cnt2 < -1:
                heapq.heappush(chs, (cnt2 + 1, ch2))

        if chs:
            res += chs[0][1]
        return res