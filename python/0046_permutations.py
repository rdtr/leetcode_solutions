class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, len(nums), result)
        return result

    def helper(self, nums, end, result):
        if end == 0:
            result.append(nums[::])
            return

        for i in range(end):
            nums[i], nums[end - 1] = nums[end - 1], nums[i]
            self.helper(nums, end - 1, result)
            nums[i], nums[end - 1] = nums[end - 1], nums[i]

