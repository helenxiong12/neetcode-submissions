from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = defaultdict(int)
        dp[-nums[0]] += 1
        dp[nums[0]] += 1

        for i in range(1, n):
            next_dp = defaultdict(int)
            for k, v in dp.items():
                next_dp[k+nums[i]] += v
                next_dp[k-nums[i]] += v
            dp = next_dp

        if target in dp:
            return dp[target]
        return 0