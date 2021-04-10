# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        
        return max_profit