
## k-1/factor(), choose k, k-1, or k+1
## Notice: no need for using sort for n_list
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        n_list = list(range(1, n + 1))
        str_list = []
        k -= 1
        for i in range(n):
            curr_idx, k = divmod(k, math.factorial(n - 1 - i))
            str_list.append(str(n_list[curr_idx]))
            n_list.remove(n_list[curr_idx])

        return ''.join(str_list)