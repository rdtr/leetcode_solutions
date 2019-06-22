class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        remaining = R * C
        right = down = 1
        up = left = 2
        directions = ['R', 'D', 'L', 'U']

        res = []
        curR, curC = r0, c0
        step = 0

        if 0 <= curR < R and 0 <= curC < C:
            res.append([curR, curC])
            remaining -= 1

        while remaining > 0:
            direction = directions[step % len(directions)]
            if direction == 'R':
                i = 0
                while remaining and i < right:
                    curC += 1
                    if 0 <= curR < R and 0 <= curC < C:
                        res.append([curR, curC])
                        remaining -= 1
                    i += 1
                right += 2
            elif direction == 'D':
                i = 0
                while remaining and i < down:
                    curR += 1
                    if 0 <= curR < R and 0 <= curC < C:
                        res.append([curR, curC])
                        remaining -= 1
                    i += 1
                down += 2
            elif direction == 'L':
                i = 0
                while remaining and i < left:
                    curC -= 1
                    if 0 <= curR < R and 0 <= curC < C:
                        res.append([curR, curC])
                        remaining -= 1
                    i += 1
                left += 2
            else:
                i = 0
                while remaining and i < up:
                    curR -= 1
                    if 0 <= curR < R and 0 <= curC < C:
                        res.append([curR, curC])
                        remaining -= 1
                    i += 1
                up += 2
            step += 1
        return res