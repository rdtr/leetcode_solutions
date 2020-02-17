from collections import deque

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        q = deque([])
        cur = 0
        if n % 2 == 1:
            q.append('0')
            q.append('1')
            q.append('8')
            cur = 1
        else:
            q.append('11')
            q.append('69')
            q.append('88')
            q.append('96')
            if n > 2:
                q.append('00')
            cur = 2
        
        while cur < n:
            qlen = len(q)
            for i in range(qlen):
                num = q.popleft()
                
                q.append('1' + num + '1')
                q.append('6' + num + '9')
                q.append('9' + num + '6')
                q.append('8' + num + '8')
                if cur != n - 2:
                    q.append('0' + num + '0')
            cur += 2
            
        return q
                
