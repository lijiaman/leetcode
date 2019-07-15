def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    total_num = len(nums)
    i = 0
    for j in range(total_num):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i

def removeElement(self, nums, val):
        """
    :type nums: List[int]
    :type val: int
    :rtype: int
        """
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1

    return i