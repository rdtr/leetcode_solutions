class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i - 1]
            res[i] *= tmp
        tmp = 1
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            res[i] *= tmp
        return res