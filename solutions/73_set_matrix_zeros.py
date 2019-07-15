def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_list = []
    col_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row_list.append(i)
                col_list.append(j)

    for r in row_list:
        matrix[r][:] = [0] * len(matrix[0])
    for c in col_list:
        for k in range(len(matrix)):
            matrix[k][c] = 0