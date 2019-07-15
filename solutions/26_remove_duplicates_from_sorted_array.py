def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_num = len(nums)
    i = 0
    for j in range(total_num):
        if j == 0:
            nums[i] = nums[j]
            i += 1
            val = nums[j]
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
            val = nums[j]

    return i