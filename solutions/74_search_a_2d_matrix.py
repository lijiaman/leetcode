class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for i in range(len(matrix)):
            flatten.extend(matrix[i])

        l = 0
        r = len(flatten) - 1
        while l <= r:
            mid = (l + r) // 2
            if flatten[mid] < target:
                l = mid + 1
            elif flatten[mid] > target:
                r = mid - 1
            else:
                return True
        return False


