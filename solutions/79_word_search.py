class Solution:
    def try_path(self, i, j, w_idx, w_list, board, str_list, visited_list):
        if not self.exist_flag:
            if len(board) == 1 and len(board[0]) == 1:
                str_list.append(board[i][j])
            if w_list == str_list:
                self.exist_flag = True
                return
            if board[i][j] != w_list[w_idx]:
                return
            if visited_list[i][j] == 1:
                return
            if j < len(board[0]) - 1:
                str_list.append(board[i][j])
                visited_list[i][j] = 1
                self.try_path(i, j + 1, w_idx + 1, w_list, board, str_list, visited_list)
                str_list.pop()
                visited_list[i][j] = 0
            if j > 0:
                str_list.append(board[i][j])
                visited_list[i][j] = 1
                self.try_path(i, j - 1, w_idx + 1, w_list, board, str_list, visited_list)
                str_list.pop()
                visited_list[i][j] = 0
            if i < len(board) - 1:
                str_list.append(board[i][j])
                visited_list[i][j] = 1
                self.try_path(i + 1, j, w_idx + 1, w_list, board, str_list, visited_list)
                str_list.pop()
                visited_list[i][j] = 0
            if i > 0:
                str_list.append(board[i][j])
                visited_list[i][j] = 1
                self.try_path(i - 1, j, w_idx + 1, w_list, board, str_list, visited_list)
                str_list.pop()
                visited_list[i][j] = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        w_list = list(word)
        idx_list = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == w_list[0]:
                    idx_list.append([i, j])

        self.exist_flag = False
        for pair_idx in idx_list:
            i, j = pair_idx
            str_list = []
            visited_list = [[0 for j in range(len(board[0]))] for i in range(len(board))]
            self.try_path(i, j, 0, w_list, board, str_list, visited_list)

        return self.exist_flag