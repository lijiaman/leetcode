class Solution:
    def dfs(self, index, str, res_str, final_list):
        if index == 4:
            if len(str) == 0:
                final_list.append(res_str[:-1])
            return
        for i in range(1, 4):
            if i <= len(str):
                if (i == 1) or (i == 2 and str[0] != "0") or (i == 3 and str[:i] <= "255" and str[0] != "0"):
                    res_str += str[:i]
                    self.dfs(index + 1, str[i:], res_str + ".", final_list)
                    res_str = res_str[:-i]

    def restoreIpAddresses(self, s: str) -> List[str]:
        final_list = []
        self.dfs(0, s, "", final_list)
        return final_list