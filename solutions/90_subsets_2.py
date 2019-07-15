class Solution:
    def dfs(self, index, n_list, res_list, final_list):
        if index >= len(n_list):
            new_res_list = res_list[:]
            new_res_list.sort()
            if new_res_list not in final_list:
                final_list.append(new_res_list)
            return
        for i in range(2):
            if i == 0:
                self.dfs(index + 1, n_list, res_list, final_list)
            if i == 1:
                res_list.append(n_list[index])
                self.dfs(index + 1, n_list, res_list, final_list)
                res_list.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        final_list = []
        self.dfs(0, nums, res_list, final_list)
        return final_list