class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        dp = [[-1 for _ in range(len(coins))]for _ in range(amount)]

        def recurse(remaining, idx):
            # print(remaining, coins[idx:], idx, path)
            if remaining == 0:
                return 1
            if remaining < 0 or idx >= len(coins): #  or coins[idx] > remaining:
                return 0
            
            if dp[remaining-1][idx] != -1:
                return dp[remaining-1][idx]

            ans = 0
            for j in range(remaining // coins[idx] + 1):
                ans += recurse(remaining - j * coins[idx], idx + 1)
            dp[remaining-1][idx] = ans
            return ans

        res = recurse(amount, 0)
        # print(dp)
        return res