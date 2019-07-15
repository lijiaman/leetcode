def lengthOfLastWord(self, s: str) -> int:
    len_cnt = 0
    w_flag = False
    for i in range(len(s)):
        chr = s[len(s) - 1 - i]
        if chr != ' ':
            w_flag = True
            len_cnt += 1
        if chr == ' ' and w_flag:
            break

    return len_cnt
