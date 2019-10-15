from functools import reduce

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = reduce(lambda x, y: x ^ y, nums)
        lsb = xor & -xor
        
        num1, num2 = 0, 0
        for num in nums:
            if num & lsb == lsb:
                num1 = num ^ num1
                continue
            num2 = num ^ num2
        return [num1, num2]