class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers approach
        #find the lowest price, iterate right pointer and find max
        l = 0
        r = 1
        max = 0
        while (r < len(prices)):
            profit = prices[r] - prices[l]
            if profit > max:
                max = profit
            elif profit < max and prices[l] > prices[r]:
                l = r #if profit < max, then we found cheaper price
            r += 1
        return max

        
                