def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def find_sum(target, sum, i, num_list, res_list, final_list):
        if target == sum:
            new_res_list = res_list[:]
            new_res_list.sort()
            if new_res_list not in final_list:
                final_list.append(new_res_list[:])
            return
        elif target < sum:
            return

        for d_idx in range(i, len(num_list)):
            # if d_idx > 0 and num_list[d_idx-1] == num_list[d_idx]:
            #     continue
            d = num_list[d_idx]
            if d > target:
                continue
            res_list.append(d)
            find_sum(target, sum + d, d_idx + 1, num_list, res_list, final_list)
            res_list.pop()

    candidates.sort()
    res_list = []
    final_list = []
    find_sum(target, 0, 0, candidates, res_list, final_list)
    return final_list