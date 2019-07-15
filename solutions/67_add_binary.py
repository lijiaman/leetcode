class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b) + 1
        res_list = [0] * max_len
        carry = 0
        for i in range(max_len):
            a_idx = len_a - 1 - i
            b_idx = len_b - 1 - i
            sum = 0
            if a_idx >= 0:
                sum += int(a[a_idx])
            if b_idx >= 0:
                sum += int(b[b_idx])

            sum += carry
            carry = sum // 2
            sum = sum % 2
            res_list[max_len - 1 - i] = str(sum)

        if len(''.join(res_list).lstrip('0')) == 0:
            return '0'
        else:
            return ''.join(res_list).lstrip('0')
