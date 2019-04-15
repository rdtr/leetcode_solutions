from collections import deque


class Solution:
    def canWin(self, s: str) -> bool:
        seen = {}
        return self.helper(s, seen)

    def helper(self, s, seen):
        if s in seen:
            return seen[s]

        win = False
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                newstr = s[:i] + '--' + s[i + 2:]
                if not self.helper(newstr, seen):  # opponent
                    win = True
        seen[s] = win
        return seen[s]
