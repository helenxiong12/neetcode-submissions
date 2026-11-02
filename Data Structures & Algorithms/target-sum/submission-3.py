from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # define:
        n = len(nums)
        # {idx, result: count}
        dp = [defaultdict(int) for _ in range(n)]
        dp[0][-nums[0]] += 1
        dp[0][nums[0]] += 1

        for i in range(1, n):
            for k, v in dp[i-1].items():
                dp[i][k+nums[i]] += v
                dp[i][k-nums[i]] += v
        # print(dp)
        for k,v in dp[-1].items():
            if k == target:
                return v
        return 0