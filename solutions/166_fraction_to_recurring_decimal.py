# 32ms(89.69%), 13.2M(77.73%)
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator*denominator < 0 else ''
        numerator, denominator = map(abs, [numerator, denominator])
        if numerator % denominator == 0:
            return sign+str(numerator//denominator)
        prefix = str(numerator//denominator)+'.'
        remainder = numerator%denominator
        r_dict = {}
        postfix = ''
        while remainder not in r_dict:
            r_dict[remainder] = len(postfix)
            postfix += str(remainder*10//denominator)
            remainder = remainder*10%denominator
            if remainder == 0:
                return sign+prefix+postfix
        return sign+prefix+postfix[:r_dict[remainder]]+'('+postfix[r_dict[remainder]:]+')'