class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                if target == nums[left] + nums[right]:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif target < nums[left] + nums[right]:
                    right -= 1
                else:
                    left += 1
        return res
