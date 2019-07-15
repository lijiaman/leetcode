class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left_i = left_j = 0
        right_i = right_j = n - 1
        res_list = [[1 for i in range(n)] for j in range(n)]
        cnt = 1
        while left_i <= right_i and left_j <= right_j and left_i < n and left_j < n and right_i > 0 and right_j > 0:
            for j in range(left_j, right_j + 1):
                res_list[left_i][j] = cnt
                cnt += 1
            for i in range(left_i + 1, right_i):
                res_list[i][right_j] = cnt
                cnt += 1
            if right_j > left_j:
                for j in range(right_j, left_j - 1, -1):
                    res_list[right_i][j] = cnt
                    cnt += 1
            if right_i > left_i:
                for i in range(right_i - 1, left_i, -1):
                    res_list[i][left_j] = cnt
                    cnt += 1
            left_i += 1
            left_j += 1
            right_i -= 1
            right_j -= 1

        return res_list