def plusOne(self, digits: List[int]) -> List[int]:
    carry = 0
    res_list = [0] * (len(digits) + 1)
    for i in range(len(digits)):
        d = digits[len(digits) - 1 - i]
        if i == 0:
            d += 1
        else:
            d += carry
        carry = d // 10
        res_list[len(digits) - i] = d % 10

    if carry:
        res_list[0] = 1
        return res_list
    else:
        return res_list[1:]