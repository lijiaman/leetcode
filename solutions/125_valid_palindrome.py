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
