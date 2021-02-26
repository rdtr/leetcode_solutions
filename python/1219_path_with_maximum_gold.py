class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        
        res = [0]
        visited = set()
        for i in range(row):
            for j in range(col):
                if (i, j) not in visited:
                    if grid[i][j] != 0:
                        visited.add((i, j))
                        self.helper(grid, i, j, visited, grid[i][j] , res)
                        visited.remove((i, j))
        return res[0]
    
    def helper(self, grid, i, j, visited, cursum, res):
        if cursum > res[0]:
            res[0] = cursum
        
        moves = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
        for x, y in moves:
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != 0:
                if (x, y) not in visited:
                    visited.add((x, y))
                    self.helper(grid, x, y, visited, cursum + grid[x][y], res)
                    visited.remove((x, y))
