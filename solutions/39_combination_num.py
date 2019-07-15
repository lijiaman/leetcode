def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def find_sum(target, sum, num_list, res_list, final_list):
        if target == sum:
            new_res_list = res_list[:]
            new_res_list.sort()
            if new_res_list not in final_list:
                final_list.append(new_res_list[:])
            return
        elif target < sum:
            return

        for d in num_list:
            res_list.append(d)
            find_sum(target, sum + d, num_list, res_list, final_list)
            res_list.pop()

    candidates.sort()
    res_list = []
    final_list = []
    find_sum(target, 0, candidates, res_list, final_list)
    return final_list