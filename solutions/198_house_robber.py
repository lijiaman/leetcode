# 1. DP with O(n) array
# 44ms(14.98%), 13.2M(42.34%)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

# 2. DP with O(1) space
# 36ms(66.91%), 13.1M(73.21%)
# 28ms(97.44%), 13M(96.85%) (same code submitted for several times, got different performance)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2] + nums[i])

        return max(dp[0], dp[1])
