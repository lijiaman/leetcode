## https://blog.csdn.net/xygy8860/article/details/46955847

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1  # for 0
        j = -1  # for 1
        k = -1  # for 2
        for idx in range(len(nums)):
            if nums[idx] == 0:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0
            elif nums[idx] == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
            elif nums[idx] == 2:
                k += 1
                nums[k] = 2
