def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """

    def solve(a, b):
        if b == 0:
            return 1
        if b == 1:
            return a
        if b < 0:
            return 1 / solve(a, -b)
        if b % 2 == 0:
            return solve(a * a, b / 2)
        else:
            return a * solve(a, b - 1)

    res = solve(x, n)
    return res