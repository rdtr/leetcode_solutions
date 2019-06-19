class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        for i in range(2 ** len(nums)):
            cur = []
            for j in range(len(nums)):
                if i & 1 == 1:
                    cur.append(nums[j])
                i = i >> 1
            res.append(cur)
        return res