class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        alen = len(A)
        odd = even = 0
        while True:
            while odd < alen and A[odd] % 2 == 0:
                odd += 1
            if odd == alen:
                break

            even = odd + 1
            while even < alen and A[even] % 2 == 1:
                even += 1
            if even == alen:
                break

            A[odd], A[even] = A[even], A[odd]
        return A