from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.mapX = defaultdict(lambda: defaultdict(lambda: 0))
        self.mapY = defaultdict(lambda: defaultdict(lambda: 0))

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.mapX[x][y] += 1
        self.mapY[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        yMap = self.mapX[x]
        xMap = self.mapY[y]

        count = 0
        for x1, countX in xMap.items():
            if countX > 0:
                for y1, countY in yMap.items():
                    if countY > 0:
                        if x != x1 and abs(x - x1) == abs(y - y1):
                            if self.mapX[x1][y1] > 0:
                                count += countX * countY * self.mapX[x1][y1]
        return count
