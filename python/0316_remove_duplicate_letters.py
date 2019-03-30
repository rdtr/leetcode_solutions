class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def idx(ch):
            return ord(ch) - ord('a')

        counter = [0] * 26
        visited = [False] * 26
        for ch in s:
            counter[idx(ch)] += 1

        stack = []
        for ch in s:
            if visited[idx(ch)]:
                counter[idx(ch)] -= 1
                continue

            while stack and ch < stack[-1] and counter[idx(stack[-1])] > 0:
                visited[idx(stack[-1])] = 0
                stack.pop()

            stack.append(ch)
            counter[idx(ch)] -= 1
            visited[idx(ch)] = True

        return ''.join(stack)
