# 1. Linear Scan (3 cases)
# 36ms(70.61%), 13.2M(44.86%)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i > 0 and i < len(nums)-1:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
            elif i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    return i

# 2. Binary Search
# 32ms(90.27%), 13.2M(54.24%)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
        return l if nums[l] > nums[r] else r


