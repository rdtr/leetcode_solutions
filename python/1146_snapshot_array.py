class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(0, 0)] for x in range(length)]
        self.ver = 0

    def set(self, index: int, val: int) -> None:
        stored = self.array[index][-1]
        if stored[1] == self.ver:
            self.array[index][-1] = (val, self.ver)
        else:
            self.array[index].append((val, self.ver))

    def snap(self) -> int:
        tmp = self.ver
        self.ver += 1
        return tmp

    def get(self, index: int, snap_id: int) -> int:
        histories = self.array[index]
        lo, hi = 0, len(histories)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if histories[mid][1] == snap_id:
                return histories[mid][0]
            elif histories[mid][1] < snap_id:
                lo = mid + 1
            else:
                hi = mid
        
        return histories[hi-1][0]