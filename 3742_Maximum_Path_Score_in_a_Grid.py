class Solution(object):
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        # dp[j][c] = max score at column j with cost c
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        # Start cell (0,0)
        dp[0][0] = 0
        
        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            
            for j in range(n):
                val = grid[i][j]
                cost = 0 if val == 0 else 1
                score = val
                
                for c in range(k + 1):
                    if c < cost:
                        continue
                    
                    best_prev = -1
                    
                    # from top
                    if i > 0:
                        best_prev = max(best_prev, dp[j][c - cost])
                    
                    # from left
                    if j > 0:
                        best_prev = max(best_prev, new_dp[j - 1][c - cost])
                    
                    # starting cell
                    if i == 0 and j == 0 and c == 0:
                        best_prev = 0
                    
                    if best_prev != -1:
                        new_dp[j][c] = max(new_dp[j][c], best_prev + score)
            
            dp = new_dp
        
        # get answer
        res = max(dp[n - 1][:k + 1])
        return res if res != -1 else -1