# 1. With python built-in function
# 4ms(99.88%), 11.7(64.76%)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

# 2.1 Bit Manipulation (>>, &1)
# 20ms(66.38%), 11.7M(78.54%)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            cnt += (n & 1)
            n >>= 1
        return cnt

# 2.2 Bit Manipulation (n & (n-1))
# 16ms(85.60%), 11.9M(5.44%)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
