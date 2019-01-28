class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        nlen = len(nums)
        if nlen == 0:
            return []

        nums.append(nums[-1])  # append a sentinel
        res = []
        for i in range(nlen + 1):
            if i == 0:
                start, end = nums[i], nums[i]
                continue

            if end + 1 == nums[i]:
                end = nums[i]
                continue

            if start == end:
                res.append(str(end))
            else:
                res.append(str(start) + "->" + str(end))
            start, end = nums[i], nums[i]
        return res
