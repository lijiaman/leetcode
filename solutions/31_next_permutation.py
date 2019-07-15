def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    total_num = len(nums)
    reverse_flag = True
    for i in range(total_num):
        curr = nums[total_num - 1 - i]
        if i < total_num - 1:
            prev = nums[total_num - 2 - i]
            if prev < curr:
                remain_list = nums[total_num - 2 - i:]
                num_remain = len(remain_list)
                for j in range(num_remain):
                    if remain_list[num_remain - 1 - j] > prev:
                        swap_idx = num_remain - 1 - j
                        break
                nums[total_num - 2 - i] = remain_list[swap_idx]
                remain_list[swap_idx] = prev
                new_remain_list = remain_list[1:]
                new_remain_list.sort()
                nums[total_num - 1 - i:] = new_remain_list[:]
                reverse_flag = False
                break

    if reverse_flag:
        nums.reverse()