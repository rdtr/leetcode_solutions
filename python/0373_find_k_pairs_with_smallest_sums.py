from heapq import heapify, heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        l1, l2 = len(nums1), len(nums2)

        if l1 == 0 or l2 == 0:
            return []
        if l1 * l2 < k:
            k = l1 * l2

        h = [HeapNode(nums1[0] + nums2[0], 0, 0)]
        heapify(h)
        visited = set([(0, 0)])

        res = []
        for _ in range(k):
            popped = heappop(h)

            if popped.j < l2 - 1 and (popped.i, popped.j + 1) not in visited:
                visited.add((popped.i, popped.j + 1))
                heappush(h, HeapNode(nums1[popped.i] + nums2[popped.j + 1], popped.i, popped.j + 1))
            if popped.i < l1 - 1 and (popped.i + 1, popped.j) not in visited:
                visited.add((popped.i + 1, popped.j))
                heappush(h, HeapNode(nums1[popped.i + 1] + nums2[popped.j], popped.i + 1, popped.j))

            res.append([nums1[popped.i], nums2[popped.j]])
        return res


class HeapNode:
    def __init__(self, val, i, j):
        self.val = val
        self.i = i
        self.j = j

    def __lt__(self, other):
        if self.val != other.val:
            return self.val < other.val

        if self.i != other.i:
            return self.i < other.i
        return self.j < other.j
