from collections import defaultdict

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        for num in nums:
            self.buildTrie(root, num)

        res = 0
        for num in nums:
            cur, node = 0, root

            for i in range(31, -1, -1):
                bit = num >> i & 1
                if (1 - bit) in node:
                    cur += 1 << i
                    node = node[1 - bit]
                    continue
                node = node[bit]
            res = max(cur, res)
        return res

    def buildTrie(self, root, num):
        cur = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in cur:
                tmp = {}
                cur[bit] = tmp
                cur = tmp
            else:
                cur = cur[bit]

