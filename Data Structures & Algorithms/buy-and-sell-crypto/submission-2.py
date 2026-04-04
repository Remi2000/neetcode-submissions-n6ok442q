class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0   # buy
        r = 1   # sell

        while l < r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r += 1
            else:
                l = r
                r = l + 1

        return max_profit

