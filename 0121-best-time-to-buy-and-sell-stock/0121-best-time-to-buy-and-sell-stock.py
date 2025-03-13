class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        
        for price in prices:
            if price < min_price:
                min_price = min(min_price, price)
            else:
                profit = max(profit, price - min_price)

        return profit
