# 1. DFS Recursively
# 84ms(57.51%), 13.8M(81.18%)
class Solution:
    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(i, j - 1, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i + 1, j, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(i, j, grid)

        return cnt

# 2. DFS Iteratively---Stack
# 56ms(98.81%), 13.8M(88.39%)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    stack = [(i, j)]
                    grid[i][j] == '0'
                    while len(stack) > 0:
                        r_idx, c_idx = stack.pop()
                        if c_idx > 0 and grid[r_idx][c_idx - 1] == '1':
                            stack.append((r_idx, c_idx - 1))
                            grid[r_idx][c_idx-1] = '0'
                        if c_idx < len(grid[0]) - 1 and grid[r_idx][c_idx + 1] == '1':
                            stack.append((r_idx, c_idx + 1))
                            grid[r_idx][c_idx+1] = '0'
                        if r_idx > 0 and grid[r_idx - 1][c_idx] == '1':
                            stack.append((r_idx - 1, c_idx))
                            grid[r_idx-1][c_idx] = '0'
                        if r_idx < len(grid) - 1 and grid[r_idx + 1][c_idx] == '1':
                            stack.append((r_idx + 1, c_idx))
                            grid[r_idx+1][c_idx] = '0'
        return cnt

# 3. BFS---Queue
# 56ms(98.85%), 13.7M(93.16%)
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    queue = collections.deque()
                    queue.append((i, j))
                    grid[i][j] = '0'
                    while len(queue) > 0:
                        r_idx, c_idx = queue.popleft()
                        if c_idx > 0 and grid[r_idx][c_idx - 1] == '1':
                            queue.append((r_idx, c_idx - 1))
                            grid[r_idx][c_idx - 1] = '0'
                        if c_idx < len(grid[0]) - 1 and grid[r_idx][c_idx + 1] == '1':
                            queue.append((r_idx, c_idx + 1))
                            grid[r_idx][c_idx + 1] = '0'
                        if r_idx > 0 and grid[r_idx - 1][c_idx] == '1':
                            queue.append((r_idx - 1, c_idx))
                            grid[r_idx - 1][c_idx] = '0'
                        if r_idx < len(grid) - 1 and grid[r_idx + 1][c_idx] == '1':
                            queue.append((r_idx + 1, c_idx))
                            grid[r_idx + 1][c_idx] = '0'
        return cnt

# 4. Union-Find(To Do)
