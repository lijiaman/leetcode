class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s.lstrip('0')) != len(s):
            return 0
        dp = [1] * len(s)
        for i in range(1, len(s)):
            if s[i - 1:i + 1] <= "26" and s[i] != "0" and s[i - 1] != "0":
                if i == 1:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i - 1:i + 1] <= "26" and s[i] == "0" and s[i - 1] != "0":
                if i == 1:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 2]
            elif s[i - 1:i + 1] <= "26" and s[i] != "0" and s[i - 1] == "0":
                if i == 1:
                    dp[i] = 0
                else:
                    dp[i] = dp[i - 1]
            else:
                if s[i] == "0":
                    dp[i] = 0
                else:
                    dp[i] = dp[i - 1]

        return dp[-1]