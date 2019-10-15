class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        curLength = 0
        maxLength = 0

        for path in input.split('\n'):
            level = 0
            i = 0
            while path[i:i + 1] == '\t':
                level += 1
                i += 1

            path = path[i:]  # remove prefix of '\t'
            while stack and len(stack) - 1 >= level:
                curLength -= len(stack[-1])
                stack.pop(-1)

            stack.append(path)
            curLength += len(path)

            if path.find('.') != -1 and curLength + len(stack) - 1 > maxLength:
                maxLength = curLength + len(stack) - 1
        return maxLength
