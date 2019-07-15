class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(i + n, max_reach)

        return True
