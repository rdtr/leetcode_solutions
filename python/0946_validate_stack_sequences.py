class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        return self.helper([], pushed, popped, 0, 0)
        
    def helper(self, cur, pushed, popped, m, n):
        if m == len(pushed) and n == len(popped):
            return True
        
        if not cur:
            if m == len(pushed):
                return False
            return self.helper([pushed[m]], pushed, popped, m + 1, n)
        
        res1 = res2 = False
        if n < len(popped) and cur[-1] == popped[n]:
            cur.pop()
            return self.helper(cur, pushed, popped, m, n + 1)
        
        if m < len(pushed):
            cur.append(pushed[m])
            return self.helper(cur, pushed, popped, m + 1, n)
        
        return False