from collections import defaultdict

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        tlen = len(tree)
        if tlen == 0:
            return 0

        left = right = 0
        res = curSum = 0
        fruitMap = defaultdict(lambda: 0)

        shouldBreak = False
        while not shouldBreak:
            while len(fruitMap.keys()) <= 2:
                fruitMap[tree[right]] += 1
                curSum += 1
                if len(fruitMap.keys()) <= 2:
                    res = max(res, curSum)
                right += 1

                if right == tlen:
                    shouldBreak = True
                    break

            while left < right and len(fruitMap.keys()) > 2:
                curSum -= 1
                fruitMap[tree[left]] -= 1
                if fruitMap[tree[left]] == 0:
                    del fruitMap[tree[left]]
                left += 1

        return res