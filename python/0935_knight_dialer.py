class Solution:
    DEST_MAP = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6]
    }

    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N <= 0:
            return 0

        prev = [1] * 10
        next = [0] * 10

        for i in range(1, N):
            for n, pad in enumerate(prev):
                next_pads = Solution.DEST_MAP[n]
                for next_pad in next_pads:
                    next[next_pad] += prev[n]

            prev = next
            next = [0] * 10
        return sum(prev) % (10 ** 9 + 7)
