class Solution:
    def solveEquation(self, equation: str) -> str:
        splits = equation.split('=')
        leftStr, rightStr = splits[0], splits[1]

        leftA, leftB = self.analyze(leftStr)
        rightA, rightB = self.analyze(rightStr)

        if leftA == rightA:
            if leftB != rightB:
                return "No solution"
            return "Infinite solutions"
        return 'x=' + str((rightB - leftB) // (leftA - rightA))

    def analyze(self, s):
        stack = []
        sign = 1

        a, b = 0, 0

        i = 0
        while i <= len(s):
            if i == 0:
                if s[i] == '-':
                    sign = -1
                    i += 1
                    continue

            if i == len(s) or s[i] == '+' or s[i] == '-':
                base = 1
                num = 0

                isA = False
                if stack[-1] == 'x':
                    isA = True
                    stack = stack[:-1]
                    if not stack:
                        num = 1

                while stack:
                    digit = stack.pop()
                    num += int(digit) * base
                    base *= 10

                if isA:
                    a += num * sign
                else:
                    b += num * sign

                if i < len(s):
                    sign = 1 if s[i] == '+' else -1
            else:
                stack.append(s[i])
            i += 1
        return a, b
