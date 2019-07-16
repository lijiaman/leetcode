# 1. DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                len_w = len(w)
                if s[i - len_w + 1:i + 1] == w and (dp[i - len_w] or i - len_w == -1):
                    dp[i] = True

        return dp[-1]

# 2. DFS (To Do)

# 3. BFS (To Do)

# 4. Trie (To Do)
