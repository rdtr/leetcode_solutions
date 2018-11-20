class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nlen = len(nums)
        visited = nlen - 1
        for i in range(nlen - 1, -1, -1):
            if i + nums[i] >= visited:
                visited = i
        return visited == 0