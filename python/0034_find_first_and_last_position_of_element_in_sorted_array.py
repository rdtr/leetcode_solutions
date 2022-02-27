class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search left
        left = len(nums)
        ng, ok = -1, len(nums)
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if self.solveLeft(mid, nums, target):
                ok = mid
            else:
                ng = mid
        left = ok

        # not found case
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        # search right
        right = -1
        ok, ng = -1, len(nums)
        while abs(ok - ng) > 1:
            mid = ok + (ng - ok) // 2
            if self.solveRight(mid, nums, target):
                ok = mid
            else:
                ng = mid
        right = ok

        # not found case
        if right == -1 or nums[right] != target:
            return [-1, -1]

        return [left, right]

    def solveLeft(self, mid, nums, target):
        return nums[mid] >= target

    def solveRight(self, mid, nums, target):
        return nums[mid] <= target
