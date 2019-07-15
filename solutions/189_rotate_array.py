# 1. Cyclic Replacements
# Time: O(n), Space: O(1)
# 48ms(77.21%), 12.1M(77.67%)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k % len(nums) == 0:
            return nums
        cnt = 0
        start = 0
        n = len(nums)
        k = k % len(nums)
        while start < n and cnt < n:
            i = start
            prev = nums[i]
            while i == start or i % n != start % n:
                tmp = nums[(i + k) % n]
                nums[(i + k) % n] = prev
                prev = tmp
                cnt += 1
                i += k
            start += 1

# 2. Reverse
# Time: O(n), Space O(1)
# 44ms(90.58%), 12M(86.45%)
class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k % len(nums) == 0:
            return nums
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

# 3. Make copy of array
# Time: O(n), Space: O(n)
# 40ms(98.04%), 12M(87.23%)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k % len(nums) == 0:
            return nums
        n = len(nums)
        r_half = nums[n - k:]
        l_half = nums[:n - k]
        nums[:k] = r_half
        nums[k:] = l_half

        return nums
