class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            if i == 0:
                dp[i][0] = grid[i][0]
            else:
                dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(n):
            if j == 0:
                dp[0][j] = grid[0][j]
            else:
                dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]