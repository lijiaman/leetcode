class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        matrix = [[1 for j in range(i + 1)] for i in range(rowIndex + 1)]
        if rowIndex == 0 or rowIndex == 1:
            return matrix[-1]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

        return matrix[-1]