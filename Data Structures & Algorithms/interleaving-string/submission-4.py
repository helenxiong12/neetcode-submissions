class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if dp[i][j] != -1:
                return dp[i][j]
            ans = False
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i+1, j):
                ans = True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j+1):
                ans = True
            dp[i][j] = 0 if ans == False else 1
            return ans

        return dfs(0, 0)
