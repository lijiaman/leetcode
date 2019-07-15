def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    if len(nums) < 3:
        return []
    res = nums[0] + nums[1] + nums[2]
    final_list = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                final_list.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1

            elif sum < 0:
                j += 1
            elif sum > 0:
                k -= 1

    return final_list
