# binary search, edge problem

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        l = 0
        r = x - 1
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid

        if mid * mid < x:
            return mid
        else:
            return mid - 1
