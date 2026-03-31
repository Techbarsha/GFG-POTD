class Solution:
    def maxProfit(self, arr, k):
        # code here
        
        # This code implemented by Barsha Saha
       
        if not arr:
            return 0
            
        hold = -arr[0]   # Buying first stock
        cash = 0         # No stock, no profit
        
        for price in arr[1:]:
            prev_hold = hold
            
            # Either keep holding OR buy today
            hold = max(hold, cash - price)
            
            # Either keep cash OR sell today (pay fee)
            cash = max(cash, prev_hold + price - k)
        
        return cash
        
        
