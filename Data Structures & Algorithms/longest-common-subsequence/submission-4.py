class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        i, j = 0, 0
        dp = [[0] * n for _ in range(m)]

        # 1. recursive
        def recurse(r, c):
            if r == m or c == n: # out of bounds
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            if text1[r] == text2[c]:
                dp[r][c] = 1 + recurse(r+1, c+1)
            else:
                dp[r][c] = max(recurse(r+1, c), recurse(r, c+1))
            return dp[r][c]
        return recurse(0, 0)


