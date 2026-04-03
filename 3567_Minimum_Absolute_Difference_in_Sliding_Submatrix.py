class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        
        # Result matrix
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                # Step 1: Collect elements
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                # Step 2: Remove duplicates
                vals = list(set(vals))
                
                # Step 3: If only one unique value
                if len(vals) <= 1:
                    ans[i][j] = 0
                    continue
                
                # Step 4: Sort
                vals.sort()
                
                # Step 5: Find minimum difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                ans[i][j] = min_diff
        
        return ans