class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        pairs = set()
        m = {}
        for i, num in enumerate(nums):
            if i == 0:
                m[num] = i
                continue

            target = num - k
            if target in m:
                pairs.add((num, target) if num <= target else (target, num))

            target = num + k
            if target in m:
                pairs.add((num, target) if num <= target else (target, num))

            m[num] = i

        return len(pairs)