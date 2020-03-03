class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]
                tmp = nums[i]
                nums[tmp-1], nums[i] = tmp, nums[tmp-1]
            else:
                i += 1
