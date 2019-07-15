# 1. Hash Map + Bit Manipulation
# 64ms(86.23%), 23.5M(95.21%)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        chr_dict = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
        mask = 0xfffff
        res = 0
        data_dict = {}
        repeat_dict = {}
        for i in range(len(s)):
            res &= mask
            res |= chr_dict[s[i]]
            if i >= 9:
                if res not in data_dict:
                    data_dict[res] = 1
                else:
                    repeat_dict[res] = i - 9
            res <<= 2
        final_list = []
        for k in repeat_dict:
            start_idx = repeat_dict[k]
            final_list.append(s[start_idx:start_idx + 10])

        return final_list


# 2. Hash Map (dictionary)
# 84ms(28.65%), 26.6M(17.46%)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        str_dict = {}
        for i in range(len(s)):
            if s[i:i + 10] not in str_dict:
                str_dict[s[i:i + 10]] = 1
            else:
                str_dict[s[i:i + 10]] += 1

        res_list = []
        for k in str_dict:
            cnt = str_dict[k]
            if cnt > 1:
                res_list.append(k)

        return res_list
