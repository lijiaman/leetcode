# 26 base.
# 32ms(97.55%), 13.4M(15.99%)
class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            sum += (ord(s[len(s)-1-i])-ord('A')+1)*(26**i)
        return sum