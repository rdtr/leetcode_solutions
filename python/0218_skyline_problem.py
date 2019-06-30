from collections import defaultdict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = []
        bulidingsById = [None for _ in range(len(buildings))]

        for i, b in enumerate(buildings):
            s, e = Height(b[0], b[2], i, True), Height(b[1], b[2], i, False)
            heights.append(s)
            heights.append(e)
            bulidingsById[i] = (s, e)
        heights.sort(key=lambda h: h.x)

        res = []
        peaks = []
        for i in range(len(heights)):
            height = heights[i]

            if height.isStart:
                heapq.heappush(peaks, height)
                if not res:
                    res.append([height.x, -peaks[0].y])
                else:
                    if res[-1][1] < -peaks[0].y:
                        if res[-1][0] == peaks[0].x:
                            res[-1][1] = -peaks[0].y
                            if len(res) >= 2 and res[-1][1] == res[-2][1]:
                                res.pop()
                        else:
                            res.append([height.x, -peaks[0].y])
                    # print(peaks[0].x, -peaks[0].y, res)
            else:
                start, _ = bulidingsById[height.id]
                start.removed = True

                while peaks and peaks[0].removed:
                    heapq.heappop(peaks)

                if not peaks:
                    if res[-1][0] == height.x:
                        res[-1][1] = 0
                    else:
                        res.append([height.x, 0])
                elif res[-1][1] > -peaks[0].y:
                    if res[-1][0] == height.x:
                        res[-1][1] = -peaks[0].y
                    else:
                        res.append([height.x, -peaks[0].y])
                    # print('e', peaks[0].x, -peaks[0].y, res)

        return res


class Height:
    def __init__(self, x, y, id, isStart):
        self.x = x
        self.y = -y
        self.id = id
        self.isStart = isStart
        self.removed = False

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False

        if self.isStart and not other.isStart:
            return False
        elif not self.isStart and other.isStart:
            return True

        return self.id < other.id