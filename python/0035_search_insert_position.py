class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nlen = len(nums)
        if nlen == 0:
            return 0

        left = -1
        right = nlen

        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        return right