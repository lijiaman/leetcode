def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    def valid_check(p_list, final_flag=False):
        left_cnt = 0
        right_cnt = 0
        for p in p_list:
            if p == '(':
                left_cnt += 1
            elif p == ')':
                right_cnt += 1

            if left_cnt < right_cnt:
                return False

        if final_flag:
            if left_cnt != right_cnt:
                return False

        return True

    def solve(i, num, res_list, final_list):
        if len(res_list) == 2 * num:
            if valid_check(res_list, True):
                final_list.append(''.join(res_list[:]))
                return True
            else:
                return False

        for p in ['(', ')']:
            res_list.append(p)
            if valid_check(res_list):
                solve(i + 1, num, res_list, final_list)
            res_list.pop()

    res_list = []
    final_list = []
    solve(0, n, res_list, final_list)

    return final_list