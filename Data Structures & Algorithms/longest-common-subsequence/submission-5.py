class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        i, j = 0, 0
        dp = [[0] * n for _ in range(m)]

        """
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
        """

        # 2. bottom-up
        m_bound, n_bound = 0, 0
        for i in range(m):
            for j in range(n):
                up = max(dp[i-1][j] if i > 0 else 0, 0)
                left = max(dp[i][j-1] if j > 0 else 0, 0)

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
                else:
                    dp[i][j] = max(up, left)
        # print(dp)
        return dp[-1][-1]

                    


