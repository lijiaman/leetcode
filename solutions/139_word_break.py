# 1.1 DP1
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                len_w = len(w)
                if s[i - len_w + 1:i + 1] == w and (dp[i - len_w] or i - len_w == -1):
                    dp[i] = True

        return dp[-1]

# 1.2 DP2

# 2. DFS

# 3. BFS

# 4. Trie
