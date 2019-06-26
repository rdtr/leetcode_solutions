class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen == 0:
            return 0

        res = sumSoFar = nums[0]
        for i in range(1, nlen):
            if sumSoFar < 0:
                sumSoFar = 0
            sumSoFar += nums[i]
            if res < sumSoFar:
                res = sumSoFar
        return res