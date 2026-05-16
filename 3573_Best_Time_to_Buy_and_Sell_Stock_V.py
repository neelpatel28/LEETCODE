class Solution(object):
    def maximumProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        flat = [0] * (k + 1)
        hold = [float('-inf')] * (k + 1)
        short = [float('-inf')] * (k + 1)
        
        for price in prices:
            for t in range(k, 0, -1):

                hold[t] = max(hold[t], flat[t - 1] - price)
                short[t] = max(short[t], flat[t - 1] + price)
                
                flat[t] = max(
                    flat[t],
                    hold[t] + price,     
                    short[t] - price     
                )
        
        return max(flat)