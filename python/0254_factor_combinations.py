class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        factors = []
        result = []
        self.helper(n, 2, factors, result)
        return result

    def helper(self, n, i, factors, result):
        while i ** 2 <= n:
            if n % i == 0:
                copy = factors[::]
                copy.append(i)
                copy.append(n // i)
                result.append(copy)

                factors.append(i)
                self.helper(n // i, i, factors, result)
                factors.pop()
            i += 1

