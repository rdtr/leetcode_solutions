class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for num in nums:
            if candidate is None:
                candidate = num
                count = 1
                continue

            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = None
        return candidate