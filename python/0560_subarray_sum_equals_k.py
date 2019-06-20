from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        sums = [0] * len(nums)
        for i in range(len(nums)):
            sums[i] = nums[i] if i == 0 else sums[i - 1] + nums[i]
            if sums[i] == k:
                res += 1

        m = defaultdict(lambda: 0)
        for i in range(len(sums)):
            target = sums[i] - k

            res += m[target]
            m[sums[i]] += 1
        return res
