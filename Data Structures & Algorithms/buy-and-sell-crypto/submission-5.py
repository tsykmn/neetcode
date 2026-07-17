class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0

        for p in range(1, len(prices)):
            buy = min(prices[p], buy)
            profit = max(profit, prices[p] - buy)
        
        return profit