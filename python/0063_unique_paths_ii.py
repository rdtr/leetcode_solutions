class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        
        dp = [[0] * n for x in range(0, m)]
        
        blocked = False
        for i in range(0, n):
            if obstacleGrid[0][i] == 1:
                blocked = True
            if blocked:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        
        blocked = False
        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                blocked = True
            if blocked:
                dp[i][0] = 0
            else:
                dp[i][0] = 1            
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]