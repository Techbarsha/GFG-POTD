class Solution:
    def maximumProfit(self, prices):
        # code here
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit
