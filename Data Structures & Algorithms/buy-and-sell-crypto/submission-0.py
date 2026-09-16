class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        postSum = [-1]
        for p in prices[::-1]:
            postSum.append(max(postSum[-1], p))
        postSum.reverse()

        profit = 0
        for i in range(len(prices)):
            if postSum[i] - prices[i] > profit:
                profit = postSum[i] - prices[i]
        return profit