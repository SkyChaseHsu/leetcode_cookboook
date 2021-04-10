# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # 所有的上升日都卖，所有的下降日都买
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        
        return profit