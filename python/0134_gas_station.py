class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        i = 0
        while i < len(gas):
            amount = 0
            j = 0
            ok = True
            while j < len(gas):
                cur = (i + j) % len(gas)
                amount += gas[cur] - cost[cur]
                if amount < 0:
                    i = i + 1 if j == 0 else i + j
                    ok = False
                    break
                j += 1
            if not ok:
                continue
            return i
        return -1
