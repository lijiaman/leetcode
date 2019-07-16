# Similar to 200 Number of Islands

# 1. DFS---Recursive
class Solution:
    def move(self, i, j, board, symbol):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != 'O':
            return
        board[i][j] = symbol
        self.move(i - 1, j, board, symbol)
        self.move(i + 1, j, board, symbol)
        self.move(i, j - 1, board, symbol)
        self.move(i, j + 1, board, symbol)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == 'O':
                        self.move(i, j, board, '#')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.move(i, j, board, 'X')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'

# 2. BFS---Queue
import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = collections.deque()
        for i in range(len(board)):
            queue.append((i, 0))
            queue.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            queue.append((0, j))
            queue.append((len(board) - 1, j))
        while queue:
            curr_i, curr_j = queue.popleft()
            if board[curr_i][curr_j] == 'O':
                board[curr_i][curr_j] = '#'
                if curr_i > 1 and board[curr_i - 1][curr_j] == 'O':
                    queue.append((curr_i - 1, curr_j))
                if curr_i < len(board) - 1 and board[curr_i + 1][curr_j] == 'O':
                    queue.append((curr_i + 1, curr_j))
                if curr_j > 1 and board[curr_i][curr_j - 1] == 'O':
                    queue.append((curr_i, curr_j - 1))
                if curr_j < len(board[0]) - 1 and board[curr_i][curr_j + 1] == 'O':
                    queue.append((curr_i, curr_j + 1))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'