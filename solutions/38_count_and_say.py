def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    res = '1'
    i = 0
    while i < n - 1:
        prev = res
        res = ''
        cnt = 1
        for j in range(1, len(prev)):
            if prev[j] != prev[j - 1]:
                res += str(cnt) + str(prev[j - 1])
                cnt = 1
            else:
                cnt += 1

        i += 1
        res += str(cnt) + prev[-1]

    return res