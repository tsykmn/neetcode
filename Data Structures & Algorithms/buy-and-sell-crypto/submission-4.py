class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, len(prices) - 1
        profit = 0
        buy, best = float("inf"), 0

        # n = len(prices) - 1

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
            
        # while left < right:
        #     # buy = min(buy, prices[n-1])
        #     # best = max(best, prices[n])
        #     buy = min(buy, prices[left])
        #     best = max(best, prices[right])
            
        #     profit = max(profit, currProfit)
        #     # n -= 1

        return profit
