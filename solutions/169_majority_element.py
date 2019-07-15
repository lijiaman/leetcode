# 0. My original simple solution with sorted array
# 80ms(6.82%), 14.3M(63.95%)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 1
        max_cnt = 1
        max_n = nums[0]
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    max_n = nums[i - 1]

        return max_n

# More interesting solutions from leetcode
# 1. Sorted Array
# 48ms(74.83%), 14.2M(93.02%)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# 2. Boyer-Moore Voting Algorithm
# 64ms(23.52%), 14.1M(98.19%)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = 0
        for i in range(len(nums)):
            if cnt == 0:
                cnt += 1
                candidate = nums[i]
            elif nums[i] == candidate:
                cnt += 1
            elif nums[i] != candidate:
                cnt -= 1

        return candidate

# 3. Hash Map
# 72ms(11.56%), 14.3M(83.98%)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data_dict = {}
        for i in range(len(nums)):
            if nums[i] not in data_dict:
                data_dict[nums[i]] = 1
            else:
                data_dict[nums[i]] += 1
            if data_dict[nums[i]] > len(nums) // 2:
                return nums[i]

# 4. Divide and Conquer
# 200ms(5.39%), 14.2M(95.35%)
class Solution:
    def majority_judge(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (l + r) // 2
        left = self.majority_judge(nums, l, mid)
        right = self.majority_judge(nums, mid + 1, r)

        if left == right:
            return left
        l_val = sum(1 for i in range(l, r + 1) if nums[i] == left)
        r_val = sum(1 for i in range(l, r + 1) if nums[i] == right)
        return left if l_val > r_val else right

    def majorityElement(self, nums: List[int]) -> int:
        return self.majority_judge(nums, 0, len(nums) - 1)

# 5. Bit Manipulation (To Do)

