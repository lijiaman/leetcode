class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res_list = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res_list[-1][1]:
                res_list[-1] = [res_list[-1][0], max(res_list[-1][1], intervals[i][1])]
            else:
                res_list.append(intervals[i])

        return res_list