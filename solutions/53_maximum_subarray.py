class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_list = []
        for i in range(len(nums)):
            if i == 0:
                sum_list.append(nums[i])
            else:
                if sum_list[i - 1] > 0:
                    sum_list.append(nums[i] + sum_list[i - 1])
                else:
                    sum_list.append(nums[i])

        return max(sum_list)