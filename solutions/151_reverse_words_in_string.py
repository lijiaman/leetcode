# 1. Built-in function
# 36ms(73.78%), 13.4M(63.46%)
class Solution:
    def reverseWords(self, s: str) -> str:
        w_list = s.split()
        w_list.reverse()
        return ' '.join(w_list)

# 2. Without built-in functions
# 64ms(5.05%), 13.3M(82.82%)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        word = ""
        final_str = ""
        for i in range(len(s)):
            if s[i] != " " and word != "" and s[i - 1] == " ":
                final_str += word[::-1] + " "
                word = s[i]
            elif s[i] != " ":
                word += s[i]

        return final_str + word[::-1]
