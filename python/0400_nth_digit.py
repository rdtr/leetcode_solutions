class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        # skip until we find a base and mul
        base = 1
        mul = 9
        start = 1
        while 1:
            if n <= base * mul:
                break
            n -= base * mul
            base += 1
            mul *= 10
            start *= 10

        # find what the number is
        count = n // base
        if n % base > 0:
            count += 1
        count -= 1

        num = start + count
        n -= count * base

        # get the digit
        for i in range(base - n):
            num //= 10
        return num % 10
