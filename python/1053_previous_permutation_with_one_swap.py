class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        alen = len(A)
        if alen == 0:
            return []

        for i in range(alen - 2, -1, -1):
            if A[i] > A[i + 1]:
                target = i + 1
                for j in range(target, alen):
                    if A[target] < A[j] < A[i]:
                        target = j
                A[i], A[target] = A[target], A[i]
                break
        return A