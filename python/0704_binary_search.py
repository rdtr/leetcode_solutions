class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nlen = len(nums)
        if nlen == 0:
            return -1

        left = -1
        right = nlen
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return -1