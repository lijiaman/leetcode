def combine(self, n: int, k: int) -> List[List[int]]:
    def solve(k, num_list, res_list, final_list):
        if len(res_list) == k:
            if res_list not in final_list:
                final_list.append(res_list[:])
            return

        for d_idx in range(len(num_list)):
            res_list.append(num_list[d_idx])
            solve(k, num_list[d_idx + 1:], res_list, final_list)
            res_list.pop()

    num_list = list(range(1, n + 1))
    res_list = []
    final_list = []
    solve(k, num_list, res_list, final_list)

    return final_list