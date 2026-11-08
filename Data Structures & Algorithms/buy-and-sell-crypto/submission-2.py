class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        max = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if (profit > max):
                    max = profit
            elif prices[r] < prices[l]:
                l = r
            r += 1
        return max
                