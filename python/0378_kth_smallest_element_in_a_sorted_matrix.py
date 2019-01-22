from heapq import heapify, heappush, heappop


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        mlen = len(matrix)
        nlen = len(matrix[0])

        h = [(matrix[0][0], 0, 0)]
        heapify(h)

        visited = set([0, 0])

        for _ in range(k):
            popped = heappop(h)

            m, n = popped[1], popped[2]
            if m < mlen - 1 and (m + 1, n) not in visited:
                visited.add((m + 1, n))
                heappush(h, (matrix[m + 1][n], m + 1, n))
            if n < nlen - 1 and (m, n + 1) not in visited:
                visited.add((m, n + 1))
                heappush(h, (matrix[m][n + 1], m, n + 1))
        else:
            return popped[0]


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        lo, hi = matrix[0][0], matrix[-1][-1]
        mid = lo + (hi - lo) // 2

        while lo < hi:
            count = 0
            for row in matrix:
                c = self.bisect_right(row, mid)
                count += c

            if k <= count:
                hi = mid
            else:
                lo = mid + 1

            mid = lo + (hi - lo) // 2
        return lo

    def bisect_right(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
