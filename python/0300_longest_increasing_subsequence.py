class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            if not tails:
                tails.append(num)
                continue

            pos = self.bisect_right(tails, num)
            if pos == 0:
                tails[0] = num
            elif pos < len(tails):
                if tails[pos - 1] != num:
                    tails[pos] = num
            elif tails[pos - 1] != num:
                tails.append(num)

        return len(tails)

    def bisect_right(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return hi