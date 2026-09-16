class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        def recurse(idx):
            if idx == len(s):
                return 1
            if dp[idx] != -1:
                return dp[idx]
            if s[idx] == '0':
                dp[idx] = 0
                return 0
            ans = 0
            if int(s[idx]) > 0 and int(s[idx]) < 10:
                ans += recurse(idx + 1)
            if int(s[idx:idx+2]) > 9 and int(s[idx:idx+2]) < 27:
                ans += recurse(idx + 2)
            dp[idx] = ans
            return ans
        return recurse(0)