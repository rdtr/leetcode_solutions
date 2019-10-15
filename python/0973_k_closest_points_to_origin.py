class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        myPoints = []
        for i, p in enumerate(points):
            myPoints.append(MyPoint(p[0] ** 2 + p[1] ** 2, i, p))

        target = K
        start = 0
        end = len(myPoints) - 1
        pos = self.partition(myPoints, start, end)
        while pos != K - 1:
            if pos < K - 1:
                start = pos + 1
                pos = self.partition(myPoints, start, end)
            else:
                end = pos - 1
                pos = self.partition(myPoints, start, end)
        myPoints = myPoints[:pos + 1]
        return [(point.p) for point in myPoints]

    def partition(self, arr, start, end):
        left = start - 1
        right = start

        pivot = arr[end]
        while right < end:
            if arr[right] < pivot:
                left += 1
                arr[left], arr[right] = arr[right], arr[left]
            right += 1

        left += 1
        arr[end], arr[left] = arr[left], arr[end]
        return left


class MyPoint:
    def __init__(self, distance, id, p):
        self.distance = distance
        self.id = id
        self.p = p

    def __lt__(self, other):
        if self.distance < other.distance:
            return True
        elif self.distance > other.distance:
            return False
        return self.id < other.id