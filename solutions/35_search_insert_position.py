def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    total_num = len(nums)
    for i in range(total_num):
        if i < total_num - 1:
            curr_val = nums[i]
            next_val = nums[i + 1]
            if target == curr_val:
                return i
            if curr_val < target and next_val > target:
                return i + 1
            elif target < curr_val:
                return i
        else:
            if target == nums[i]:
                return i
            else:
                if target < nums[i]:
                    return i
                else:
                    return i + 1