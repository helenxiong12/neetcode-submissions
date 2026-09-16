class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i + 1 < len(s):
                if s[i] == '1' or s[i] == '2' and s[i+1] in "0123456":
                    dp[i] += dp[i+2]
        return dp[0]

        """    
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
        """