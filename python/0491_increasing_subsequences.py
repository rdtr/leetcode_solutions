class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        added = set()
        for i, num in enumerate(nums):
            if num not in added:
                self.doFindSussequences(nums, i, [num], res)
                added.add(num)
        return res
    
    def doFindSussequences(self, nums, i, cur, res):
        if len(cur) > 1:
            res.append(cur[:])
        if i == len(nums) - 1:
            return
        
        added = set()
        for j in range(i+1, len(nums)):
            num = nums[j]
            if num not in added:
                if cur[-1] <= num:
                    cur.append(num)
                    self.doFindSussequences(nums, j, cur, res)
                    cur.pop()    
                added.add(num)