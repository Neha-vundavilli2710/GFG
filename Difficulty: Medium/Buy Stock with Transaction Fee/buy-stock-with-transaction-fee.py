class Solution:
    def maxProfit(self, arr, k):
        
        n = len(arr)
        
        hold = -arr[0]   # buy first stock
        cash = 0         # no stock
        
        for i in range(1, n):
            price = arr[i]
            
            # update states
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - k)
        
        return cash