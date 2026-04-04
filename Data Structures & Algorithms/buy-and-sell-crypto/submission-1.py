class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time complexity O(n)
        # space complexity O(1)
        l, r = 0, 1 # left: buy      right: sell
        maxP = 0

        while l < r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP