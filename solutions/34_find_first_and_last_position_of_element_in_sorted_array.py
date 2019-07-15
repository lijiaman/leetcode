def searchRange(self, nums: List[int], target: int) -> List[int]:
    def b_search(n_list, t, left_flag):
        low = 0
        high = len(n_list)
        while low < high:
            mid = int((low + high) / 2)
            if left_flag:
                if n_list[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            else:
                if n_list[mid] <= target:
                    low = mid + 1
                else:
                    high = mid
        return low

    left = b_search(nums, target, True)
    right = b_search(nums, target, False)

    if left == len(nums) or nums[left] != target:
        return [-1, -1]

    return [left, right - 1]