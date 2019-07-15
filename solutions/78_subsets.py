def subsets(self, nums: List[int]) -> List[List[int]]:
    def solve(n, num_list, res_list, final_list):
        if len(num_list) == 0:
            if res_list not in final_list:
                final_list.append(res_list[:])
            return

        for d_idx in range(len(num_list)):
            for opt in [0, 1]:
                if opt == 1:
                    res_list.append(num_list[d_idx])
                    solve(n, num_list[d_idx + 1:], res_list, final_list)
                    res_list.pop()
                else:
                    solve(n, num_list[d_idx + 1:], res_list, final_list)

    res_list = []
    final_list = []
    solve(len(nums), nums, res_list, final_list)
    return final_list