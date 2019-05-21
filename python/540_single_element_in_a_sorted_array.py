class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nlen = len(nums)
        if nlen == 1:
            return nums[0]

        lo, hi = 0, nlen - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (mid == 0 and nums[mid] < nums[mid + 1]) or (mid == nlen - 1 and nums[mid - 1] < nums[mid]):
                return nums[mid]
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            else:
                l = hi - lo + 1
                if (l // 2) % 2 == 1:
                    if nums[mid] == nums[mid + 1]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if nums[mid] == nums[mid + 1]:
                        lo = mid + 2
                    else:
                        hi = mid - 2
        return nums[lo]
