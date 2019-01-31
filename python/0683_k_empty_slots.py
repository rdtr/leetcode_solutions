class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

        days = [0] * len(flowers)
        for day, flower in enumerate(flowers):
            days[flower - 1] = day

        res = -1
        left, right = 0, k + 1
        while right < len(days):
            later = max(days[left], days[right])
            satisfied = True

            for i in range(left + 1, right):
                if days[i] <= later:
                    left, right = i, i + k + 1
                    satisfied = False
                    break

            if not satisfied:
                continue

            res = min(later + 1, res) if res != -1 else later + 1
            left, right = right, right + k + 1
        return res