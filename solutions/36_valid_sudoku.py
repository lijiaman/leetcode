def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    def valid_check(all_list):
        d_list = []
        for i in all_list:
            if i != '.':
                d_list.append(i)
        if len(list(set(d_list))) != len(d_list):
            return False
        else:
            return True

    def row_check(board):
        for row in board:
            if not valid_check(row):
                return False
        return True

    def col_check(board):
        for col in zip(*board):
            if not valid_check(col):
                return False
        return True

    def sub_block_check(board):
        for i in range(3):
            for j in range(3):
                sub_list = []
                for b_i in range(i * 3, i * 3 + 3):
                    for b_j in range(j * 3, j * 3 + 3):
                        if board[b_i][b_j] != '.':
                            sub_list.append(board[b_i][b_j])
                if not len(list(set(sub_list))) == len(sub_list):
                    return False
        return True

    if row_check(board) and col_check(board) and sub_block_check(board):
        return True
    else:
        return False