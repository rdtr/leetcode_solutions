class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        res = [0] * (num + 1)
        if num >= 1:
            res[1] = 1
        if num >= 2:
            res[2] = 1

        i = 3
        high = 2
        while i <= num:
            while i >= high << 1:
                high = high << 1
            res[i] = 1 + res[i - high]
            i += 1

        return res