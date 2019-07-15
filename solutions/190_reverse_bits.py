# Bit manipulation
# 20ms(70.55%), 11.8M(12.32%)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1

        return res
