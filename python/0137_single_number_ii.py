class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            
            if count % 3 == 1:
                res |= (count % 3) << i
        
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res