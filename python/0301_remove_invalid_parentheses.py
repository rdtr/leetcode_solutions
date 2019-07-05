from collections import defaultdict, deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if self.isValid(s):
            return [s]

        q = deque([(s, 0)])
        found = False

        res = []
        seen = set()
        while q:
            qlen = len(q)
            for i in range(qlen):
                t, i = q.popleft()
                for j in range(i, len(t)):
                    newstr = t[:j] + t[j + 1:]
                    if newstr in seen:
                        continue
                    seen.add(newstr)

                    if self.isValid(newstr):
                        res.append(newstr)
                        found = True
                    else:
                        q.append((newstr, j))
            if found:
                break
        return res

    def isValid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                if count <= 0:
                    return False
                count -= 1
        return count == 0



