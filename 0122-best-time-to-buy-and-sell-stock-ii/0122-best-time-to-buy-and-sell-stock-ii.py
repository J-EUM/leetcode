class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 커질때만 뒤-앞
        total = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                total += profit
        return total