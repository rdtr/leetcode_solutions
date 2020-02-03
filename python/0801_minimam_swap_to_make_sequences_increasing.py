class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        DP_S = [0 for _ in range(len(A))]
        DP_NS = [0 for _ in range(len(A))]

        for i in range(len(A)):
            if i == 0:
                DP_S[i] = 1
                continue

            if A[i] <= A[i-1] or B[i] <= B[i-1]:
                DP_S[i] = DP_NS[i-1] + 1
                DP_NS[i] = DP_S[i-1]
            elif A[i] <= B[i-1] or B[i] <= A[i-1]:
                DP_S[i] = DP_S[i-1] + 1
                DP_NS[i] = DP_NS[i-1]
            else:
                DP_S[i] = min(DP_S[i-1], DP_NS[i-1]) + 1
                DP_NS[i] = min(DP_S[i-1], DP_NS[i-1])
        return min(DP_S[-1], DP_NS[-1])
