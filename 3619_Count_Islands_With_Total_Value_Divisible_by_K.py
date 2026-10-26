class Solution:
    def countIslands(self, grid, k):
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] <= 0:
                return 0
                
            cell_value = grid[r][c]
            grid[r][c] = 0 
            
            total_sum = cell_value
            total_sum += dfs(r + 1, c)
            total_sum += dfs(r - 1, c)
            total_sum += dfs(r, c + 1)
            total_sum += dfs(r, c - 1)
            
            return total_sum

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        island_count += 1
                        
        return island_count
