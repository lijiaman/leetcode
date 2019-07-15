def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    data_dict = {}
    data_dict['2'] = ['a', 'b', 'c']
    data_dict['3'] = ['d', 'e', 'f']
    data_dict['4'] = ['g', 'h', 'i']
    data_dict['5'] = ['j', 'k', 'l']
    data_dict['6'] = ['m', 'n', 'o']
    data_dict['7'] = ['p', 'q', 'r', 's']
    data_dict['8'] = ['t', 'u', 'v']
    data_dict['9'] = ['w', 'x', 'y', 'z']

    def solve(i, n, d_idx, d_list, res_list, final_list):
        if len(res_list) == n:
            final_list.append(''.join(res_list[:]))
            return True

        d = d_list[d_idx]
        a_list = data_dict[d]
        for a in a_list:
            res_list.append(a)
            solve(i + 1, n, d_idx + 1, d_list, res_list, final_list)
            res_list.pop()

    res_list = []
    final_list = []
    n = len(digits)
    if n == 0:
        return []
    solve(0, n, 0, list(digits), res_list, final_list)

    return final_list