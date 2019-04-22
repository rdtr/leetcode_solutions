class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        alen = len(A)
        if alen < 3 or A[0] >= A[1]:
            return False

        i = 2
        while i < alen:
            if A[i] > A[i - 1]:
                i += 1
                continue
            elif A[i] == A[i - 1]:
                return False
            break

        if i == alen:
            return False

        while i + 1 < alen:
            if A[i] <= A[i + 1]:
                return False
            i += 1
        return True