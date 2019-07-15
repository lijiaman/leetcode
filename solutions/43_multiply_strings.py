def multiply(self, num1: str, num2: str) -> str:
    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1
    for i in reversed(num1):
        curr_pos = pos
        for j in reversed(num2):
            product[curr_pos] += int(i) * int(j)
            if curr_pos > 0:
                product[curr_pos - 1] += product[curr_pos] // 10
            product[curr_pos] = product[curr_pos] % 10
            curr_pos -= 1

        pos -= 1

    start = 0
    while start < len(product) - 1 and product[start] == 0:
        start += 1

    return ''.join(map(str, product[start:]))