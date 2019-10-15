class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []
        self.doCombine(n, k, 1, [], res)
        return res
        
    def doCombine(self, n, k, curNum, cur, res):
        # when we don't have enough remaining number, we should stop the recursion
        if len(cur) + (n - curNum + 1) < k:
            return
        elif len(cur) == k:
            res.append(cur.copy())
            return
        
        for i in range(curNum, n + 1):
            cur.append(i)
            self.doCombine(n, k, i + 1, cur, res)
            cur.pop()