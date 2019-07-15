class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        left_i = left_j = 0
        right_i = len(matrix) - 1
        right_j = len(matrix[0]) - 1
        res_list = []
        while left_j <= right_j and left_i <= right_i and left_j < len(matrix[0]) and left_i < len(
                matrix) and right_i >= 0 and right_j >= 0:
            for j in range(left_j, right_j + 1):
                res_list.append(matrix[left_i][j])
            for i in range(left_i + 1, right_i):
                res_list.append(matrix[i][right_j])
            if left_i != right_i:
                for j in range(right_j, left_j - 1, -1):
                    res_list.append(matrix[right_i][j])
            if left_j != right_j:
                for i in range(right_i - 1, left_i, -1):
                    res_list.append(matrix[i][left_j])
            left_i += 1
            left_j += 1
            right_i -= 1
            right_j -= 1

        return res_list