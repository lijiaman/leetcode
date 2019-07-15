# Stack
# 44ms(72.06%), 13.4M(28.75%)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opt_list = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in opt_list:
                stack.append(int(tokens[i]))
            else:
                d2 = stack.pop()
                d1 = stack.pop()
                if tokens[i] == '+':
                    res = d1 + d2
                elif tokens[i] == '-':
                    res = d1 - d2
                elif tokens[i] == '*':
                    res = d1 * d2
                elif tokens[i] == '/':
                    res = int(d1 / d2)
                stack.append(res)

        return stack[-1]
