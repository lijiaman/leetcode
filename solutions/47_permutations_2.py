def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def solve(i, n, num_list, res_list, final_list):
        if len(res_list) == n:
            if res_list not in final_list:
                final_list.append(res_list[:])
            return

        for k in num_list:
            res_list.append(k)
            new_num_list = num_list[:]
            new_num_list.remove(k)
            solve(i + 1, n, new_num_list, res_list, final_list)
            res_list.pop()

    res_list = []
    n = len(nums)
    nums.sort()
    final_list = []
    solve(0, n, nums, res_list, final_list)
    return final_list