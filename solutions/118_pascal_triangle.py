class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [[1 for j in range(i + 1)] for i in range(numRows)]
        if numRows == 1 or numRows == 2:
            return matrix
        for i in range(2, numRows):
            for j in range(1, i):
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

        return matrix