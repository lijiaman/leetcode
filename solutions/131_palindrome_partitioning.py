# 1. DFS
class Solution:
    def isPalindrome(self, str):
        if len(str) == 1:
            return True
        for i in range(len(str)):
            if str[i] != str[len(str) - 1 - i]:
                return False
        return True
        # More concise: return s == s[::-1]

    def dfs(self, str, res_list, final_list):
        if len(str) == 0:
            final_list.append(res_list[:])
            return
        for i in range(1, len(str) + 1):
            if self.isPalindrome(str[:i]):
                res_list.append(str[:i])
                self.dfs(str[i:], res_list, final_list)
                res_list.pop()

    def partition(self, s: str) -> List[List[str]]:
        res_list = []
        final_list = []
        self.dfs(s, res_list, final_list)
        return final_list