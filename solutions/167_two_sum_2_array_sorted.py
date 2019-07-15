# 1. Dictionary
# 28ms(99.73%), 13.4M(98.01%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data_dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in data_dict:
                return [data_dict[target - numbers[i]] + 1, i + 1]
            if numbers[i] not in data_dict:
                data_dict[numbers[i]] = i

# 2. Two Pointer
# 40ms(72.17%), 13.6M(65.71%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1

        return []

# 3. Binary Search
# 68ms(12.57%), 13.6M(65.71%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tmp_target = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == tmp_target:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp_target:
                    l = mid + 1
                elif numbers[mid] > tmp_target:
                    r = mid - 1
        return []
