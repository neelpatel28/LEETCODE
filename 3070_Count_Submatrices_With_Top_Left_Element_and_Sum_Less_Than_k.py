class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Compute prefix sum in-place
        for i in range(m):
            for j in range(n):
                # Add top
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                
                # Add left
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                
                # Remove double counted
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                
                # Check condition
                if grid[i][j] <= k:
                    count += 1
        
        return count