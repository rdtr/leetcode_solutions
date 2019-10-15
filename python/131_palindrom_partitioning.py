class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        cache = {}
        res = []
        cur = []
        idx = 0
        self.do_partition(s, idx, cur, res, cache)
        return res

    def do_partition(self, s, idx, cur, res, cache):
        if idx == len(s):
            res.append(cur[:])
            return

        for i in range(idx + 1, len(s) + 1):
            tmp = s[idx:i]
            if tmp not in cache:
                cache[tmp] = self.check_partition(tmp)

            if not cache[tmp]:
                continue

            cur.append(tmp)
            self.do_partition(s, i, cur, res, cache)
            cur.pop()

    def check_partition(self, s):
        if len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
