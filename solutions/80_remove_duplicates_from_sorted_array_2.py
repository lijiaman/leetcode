class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        cnt = 0
        i = 2
        while i < len(nums) - cnt:
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                nums[i:-1] = nums[i + 1:]
                cnt += 1
            else:
                i += 1
            # print(nums)

        return len(nums) - cnt