## Similar to 200 Number of Islands, dfs

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
