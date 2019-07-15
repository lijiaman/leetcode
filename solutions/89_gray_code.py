## Too slow!!!

class Solution:
    def get_candidates(self, str):
        s_list = []
        for i in range(len(str)):
            if str[i] == '1':
                s_list.append(str[:i] + '0' + str[i + 1:])
            elif str[i] == '0':
                s_list.append(str[:i] + '1' + str[i + 1:])
        return s_list

    def dfs(self, str, visited_list, res_list, final_list, n):
        if len(res_list) == 2 ** n - 1:
            self.find_flag = True
            final_list.append(res_list[:])
            return
        if not self.find_flag:
            candidates = self.get_candidates(str)
            for c in candidates:
                if c not in visited_list:
                    # visited_dict[c] = 1
                    res_list.append(int(c, 2))
                    # res_list.append(c)
                    visited_list.append(c)
                    self.dfs(c, visited_list, res_list, final_list, n)
                    res_list.pop()
                    visited_list.pop()
            return

    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res_list = []
        final_list = []
        start_str = "0" * n
        visited_list = [start_str]
        self.find_flag = False
        self.dfs(start_str, visited_list, res_list, final_list, n)
        res = [int(start_str, 2)]
        res.extend(final_list[0])
        return res