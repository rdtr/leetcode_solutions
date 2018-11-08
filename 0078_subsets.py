class Solution:
    def subsets(self, nums):
        res, nlen = [[]], len(nums)

        for i in range(nlen):
            res.append([nums[i]])
            self._subsets(nums, res, [nums[i]], i)
        return res

    def _subsets(self, nums, res, cur, prev):
        if prev + 1 == len(nums):
            return

        for i in range(prev + 1, len(nums)):
            newCur = cur.copy()
            newCur.append(nums[i])
            res.append(newCur)
            self._subsets(nums, res, newCur, i)