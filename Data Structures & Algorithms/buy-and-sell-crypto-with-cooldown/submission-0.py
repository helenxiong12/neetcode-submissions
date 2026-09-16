BUY = 0
HOLD = 1
SELL = 2
WAIT = 3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recurse(day, state, profit, buy_price=-1):
            if day == len(prices):
                return profit
            elif state == BUY:
                hold_profit = recurse(day+1, HOLD, profit, prices[day])
                sell_profit = recurse(day+1, SELL, profit, prices[day])
                return max(hold_profit, sell_profit)
            elif state == HOLD:
                hold_profit = recurse(day+1, HOLD, profit, buy_price)
                sell_profit = recurse(day+1, SELL, profit, buy_price)
                return max(hold_profit, sell_profit)
            elif state == SELL:
                assert buy_price > -1
                profit += prices[day] - buy_price
                return recurse(day+1, WAIT, profit)
            elif state == WAIT:
                wait_profit = recurse(day+1, WAIT, profit)
                buy_profit = recurse(day+1, BUY, profit)
                return max(wait_profit, buy_profit)
            else:
                raise Exception("Invalid state")
        return recurse(-1, WAIT, 0)


        