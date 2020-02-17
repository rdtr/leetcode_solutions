from itertools import permutations


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        for perm in permutations(points):
            if self.dist(perm[0], perm[1]) == self.dist(perm[1], perm[2]) and self.dist(perm[1], perm[2]) == self.dist(perm[2], perm[3]) and self.dist(perm[2], perm[3]) == self.dist(perm[3], perm[0]) and self.dist(perm[3], perm[0]) == self.dist(perm[0], perm[1]) and self.dist(perm[0], perm[2]) == self.dist(perm[1], perm[3]) and self.dist(perm[0], perm[1]) < self.dist(perm[0], perm[2]):
                return True
        return False

    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
