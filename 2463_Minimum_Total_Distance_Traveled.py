class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)
        
        n = len(robot)
        m = len(slots)
        
        memo = {}
        
        def dp(i, j):
            if i == n:
                return 0
            if j == m:
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = dp(i, j + 1)
            res = min(res, dp(i + 1, j + 1) + abs(robot[i] - slots[j]))
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)