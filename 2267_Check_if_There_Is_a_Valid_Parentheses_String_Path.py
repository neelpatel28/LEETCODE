2267.class Solution(object):
    def hasValidPath(self, grid):
        if not grid or not grid[0]:
            return False
            
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        memo = {}
        
        def dfs(r, c, balance):
            if r >= m or c >= n:
                return False
                
            balance += 1 if grid[r][c] == '(' else -1
            
            if balance < 0:
                return False
                
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            state = (r, c, balance)
            if state in memo:
                return memo[state]
                
            res = dfs(r + 1, c, balance) or dfs(r, c + 1, balance)
            memo[state] = res
            return res

        return dfs(0, 0, 0)
