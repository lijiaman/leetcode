def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def find_sum(left, right, cnt, fix_cnt, target, num_list, res_list, final_list):
        if right - left + 1 < cnt or len(res_list) > fix_cnt:
            return False

        if cnt == 2:
            while left < right:
                l_val = num_list[left]
                r_val = num_list[right]
                if l_val + r_val < target:
                    left += 1
                elif l_val + r_val > target:
                    right -= 1
                else:
                    res_list.append(l_val)
                    res_list.append(r_val)
                    if len(res_list) == fix_cnt:
                        final_list.append(res_list[:])
                        res_list.pop()
                        res_list.pop()
                    while left < right and num_list[left] == num_list[left + 1]:
                        left += 1
                    while left < right and num_list[right - 1] == num_list[right]:
                        right -= 1
                    left += 1
                    right -= 1
        else:
            for i in range(left, right):
                if i == left or num_list[i - 1] != num_list[i]:
                    res_list.append(num_list[i])
                    find_sum(i + 1, right, cnt - 1, fix_cnt, target - num_list[i], num_list, res_list, final_list)
                    res_list.pop()

    nums.sort()
    n = len(nums)
    res_list = []
    final_list = []
    find_sum(0, n - 1, 4, 4, target, nums, res_list, final_list)
    return final_list