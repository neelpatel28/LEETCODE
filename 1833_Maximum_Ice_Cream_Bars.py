class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        
        for cost in costs:
            count[cost] += 1
        
        bars_bought = 0
        for cost in range(max_cost + 1):
            if count[cost] > 0:
                bars_at_this_price = min(count[cost], coins // cost)
                bars_bought += bars_at_this_price
                coins -= bars_at_this_price * cost
                if coins == 0:
                    break
        
        return bars_bought
