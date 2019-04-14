class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        primitives = []
        count = 0

        start = 0
        for i, ch in enumerate(S):
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1

            if i != 0 and count == 0:
                primitives.append(S[start + 1:i])
                start = i + 1

        return ''.join(primitives)