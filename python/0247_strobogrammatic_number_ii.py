from collections import deque


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n <= 0:
            return ''
        elif n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ['11', '69', '88', '96']

        prev2 = deque(['0', '1', '8'])
        prev1 = deque(['11', '69', '88', '96', '00'])

        k = 3
        while k <= n:
            if k % 2 == 1:
                prev2len = len(prev2)
                for i in range(prev2len):
                    val = prev2.popleft()
                    prev2.append('0' + val + '0')
                    prev2.append('1' + val + '1')
                    prev2.append('8' + val + '8')
                    prev2.append('6' + val + '9')
                    prev2.append('9' + val + '6')
                    res = prev2
            else:
                prev1len = len(prev1)
                for i in range(prev1len):
                    val = prev1.popleft()
                    prev1.append('0' + val + '0')
                    prev1.append('1' + val + '1')
                    prev1.append('8' + val + '8')
                    prev1.append('6' + val + '9')
                    prev1.append('9' + val + '6')
                    res = prev1
            k += 1
        return [val for val in res if val[0] != '0']

