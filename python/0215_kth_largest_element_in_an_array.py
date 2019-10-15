class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        n = self.partition(nums, 0, len(nums) - 1)

        while n != target:
            if n > target:
                n = self.partition(nums, 0, n - 1)
            elif n < target:
                n = self.partition(nums, n + 1, len(nums) - 1)
        return nums[n]

    def partition(self, nums, start, end):
        left, right = start - 1, start
        pivot = nums[end]
        while right < end:
            if nums[right] <= pivot:
                left += 1
                nums[right], nums[left] = nums[left], nums[right]
            right += 1

        left += 1
        nums[left], nums[end] = nums[end], nums[left]
        return left