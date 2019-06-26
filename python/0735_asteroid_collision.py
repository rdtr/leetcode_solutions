class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
            elif (asteroids[i] > 0 and stack[-1] > 0) or (asteroids[i] < 0 and stack[-1] < 0) or (
                    asteroids[i] > 0 and stack[-1] < 0):
                stack.append(asteroids[i])
            else:
                size = -asteroids[i]
                if size > stack[-1]:
                    stack.pop()
                    continue
                elif size == stack[-1]:
                    stack.pop()
            i += 1
        return stack
