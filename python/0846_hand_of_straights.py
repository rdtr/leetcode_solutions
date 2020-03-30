class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hlen = len(hand)

        hand.sort()
        pq = []
        for i in range(hlen):
            h = hand[i]
            if not pq:
                heapq.heappush(pq, (h, 1))
                continue

            smallest, count = pq[0]
            while count == W and pq:
                heapq.heappop(pq)
                if pq:
                    smallest, count = pq[0]

            if not pq:
                heapq.heappush(pq, (h, 1))
                continue

            if smallest + 1 == h:
                heapq.heappushpop(pq, (h, count + 1))
            else:
                heapq.heappush(pq, (h, 1))

        for o in pq:
            if o[1] != W:
                return False
        return True
