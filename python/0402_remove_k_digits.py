class Solution:
    def removeKdigits(self, num: 'str', k: 'int') -> 'str':
        nlen = len(num)
        count = nlen - k

        stack = []
        for i, ch in enumerate(num):
            while stack and ch < stack[-1] and len(stack) - 1 + nlen - i >= count:
                stack.pop()
            if len(stack) < count:
                stack.append(ch)

        res = ''
        for i, digit in enumerate(stack):
            if not res and digit == '0':
                continue
            res += digit
        return res if res else '0'
