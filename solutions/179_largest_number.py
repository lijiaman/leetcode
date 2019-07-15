# 1. Built-in sort with modified key
# 36ms(94.95%), 13.2M(49.59%)
import functools
class Solution:
    def compare(self, a, b):
        if a + b > b + a:
            return 1
        elif a + b == b + a:
            return 0
        else:
            return -1

    def largestNumber(self, nums: List[int]) -> str:
        str_list = []
        for n in nums:
            str_list.append(str(n))

        str_list.sort(key=functools.cmp_to_key(self.compare), reverse=True)
        return ''.join(str_list).lstrip('0') or '0'

# 2. Bubble Sort
# 108ms(6.35%), 13.4M(6.23%)
# Time: O(n^2)
class Solution:
    def compare(self, a, b):
        return (a + b) > (b + a)

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if not self.compare(str(nums[j]), str(nums[j + 1])):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return ''.join(map(str, nums)).lstrip('0') or '0'

# 3. Selection Sort
# 88ms(8.34%), 13.2M(44.72%)
# Time: O(n^2)
class Solution:
    def compare(self, a, b):
        return (a + b) > (b + a)

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        for i in range(len(nums), 0, -1):
            min_idx = i-1
            for j in range(i-1):
                if not self.compare(str(nums[j]), str(nums[min_idx])):
                    min_idx = j
            if min_idx != i-1:
                nums[min_idx], nums[i-1] = nums[i-1], nums[min_idx]
        return ''.join(map(str, nums)).lstrip('0') or '0'

# 4. Insertion Sort
# 72ms(11.17%), 13.2M(59.89%)
# Time: O(n^2)
class Solution:
    def compare(self, a, b):
        return (a + b) > (b + a)

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        for i in range(1, len(nums)):
            curr_val = nums[i]
            pos = i - 1
            while pos >= 0 and not self.compare(str(nums[pos]), str(curr_val)):
                nums[pos + 1] = nums[pos]
                pos -= 1
            nums[pos + 1] = curr_val

        return ''.join(map(str, nums)).lstrip('0') or '0'

# 5. Quick Sort
# 48ms(38.40%), 13.1M(75.00%)
# Time: O(nlogn)
class Solution:
    def compare(self, a, b):
        return (a + b) > (b + a)

    def quickSort(self, nums, l, r):
        start, end = l, r
        if l > r:
            return
        key = nums[l]
        while l < r:
            while l < r and self.compare(str(key), str(nums[r])):
                r -= 1
            if l < r:
                nums[l] = nums[r]
            while l < r and not self.compare(str(key), str(nums[l])):
                l += 1
            if l < r:
                nums[r] = nums[l]
        if l == r:
            nums[l] = key
        self.quickSort(nums, start, l - 1)
        self.quickSort(nums, l + 1, end)

        return nums

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        res_list = self.quickSort(nums, 0, len(nums) - 1)
        return ''.join(map(str, res_list)).lstrip('0') or '0'

# 6. Merge Sort
# 48ms(38.79%), 13.1M(75.56%)
# Time: O(nlogn)
class Solution:
    def compare(self, a, b):
        return (a + b) > (b + a)

    def merge(self, s1, s2):
        len_1 = len(s1)
        len_2 = len(s2)
        i = 0
        j = 0
        merged_list = []
        while i < len_1 and j < len_2:
            if not self.compare(str(s1[i]), str(s2[j])):
                merged_list.append(s2[j])
                j += 1
            else:
                merged_list.append(s1[i])
                i += 1
        merged_list.extend(s1[i:] or s2[j:])
        return merged_list

    def mergeSort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = (l + r) // 2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(left, right)

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        res_list = self.mergeSort(nums, 0, len(nums) - 1)

        return ''.join(map(str, res_list)).lstrip('0') or '0'

# 7. Heap Sort (To Do)


