class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Column-wise accumulators
        col_sum = [0] * n   # stores (X - Y)
        col_x = [0] * n     # stores count of X
        
        count = 0
        
        for i in range(m):
            row_sum = 0
            row_x = 0
            
            for j in range(n):
                # Convert character
                if grid[i][j] == 'X':
                    val = 1
                    x_val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                    x_val = 0
                else:
                    val = 0
                    x_val = 0
                
                col_sum[j] += val
                col_x[j] += x_val
                
                row_sum += col_sum[j]
                row_x += col_x[j]
                
                # Check both conditions
                if row_sum == 0 and row_x > 0:
                    count += 1
        
        return count