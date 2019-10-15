class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
                continue
            m[n] = 1

        buckets = [[] for i in range(len(nums))]
        for key, val in m.items():
            buckets[val - 1].append(key)

        res = []
        for bucket in buckets[::-1]:
            for bucket_num in bucket:
                if len(res) == k:
                    return res
                res.append(bucket_num)
        return res
