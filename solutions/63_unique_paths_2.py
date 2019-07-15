class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    dp[k][0] = 0
                break

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for k in range(j, n):
                    dp[0][k] = 0
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i - 1][j] == 1:
                    dp[i][j] = dp[i][j - 1]
                elif obstacleGrid[i][j - 1] == 1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]