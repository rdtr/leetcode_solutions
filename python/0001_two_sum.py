class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            if target-num in m:
                return (m[target-num], i)
            m[num] = i
