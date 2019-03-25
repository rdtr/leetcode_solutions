class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:
                hi = mid
            elif target == nums[mid]:
                return mid
            else:
                lo = mid + 1
        return lo
