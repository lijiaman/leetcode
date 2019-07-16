# 1. My original solution which need a new string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        s = s.lower()
        new_s = ''
        for chr in s:
            if ord(chr) >= ord('a') and ord(chr) <= ord('z'):
                new_s += chr
            if ord(chr) >= ord('0') and ord(chr) <= ord('9'):
                new_s += chr

        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False

        return True

# 2. Two pointer solution. O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        s = s.lower()

        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

