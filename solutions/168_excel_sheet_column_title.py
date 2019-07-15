# Base 26, start from index 1. Different from base 10 start from index 0.
# 36ms(62.82%), 13.2M(40.68%)
class Solution:
    def convertToTitle(self, n: int) -> str:
        chr_list = []
        for c in range(ord('A'), ord('Z') + 1):
            chr_list.append(chr(c))

        res_list = []
        while n:
            cnt = (n - 1) % 26
            n = (n - 1) // 26
            res_list.append(chr_list[cnt])

        res_list.reverse()
        return ''.join(res_list)
