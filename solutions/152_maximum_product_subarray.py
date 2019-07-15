# 48ms(48.25%), 13.4M(51.31%)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_p = big = small = nums[0]
        for i in range(1, len(nums)):
            big, small = max(nums[i], big * nums[i], small * nums[i]), min(nums[i], big * nums[i], small * nums[i])
            if big > max_p:
                max_p = big

        return max_p