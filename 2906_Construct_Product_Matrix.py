class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        
        n, m = len(grid), len(grid[0])
        
        # Flatten the grid
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)
        
        size = len(arr)
        
        # Prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Suffix product
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Result array
        result = [0] * size
        for i in range(size):
            result[i] = (prefix[i] * suffix[i]) % MOD
        
        # Convert back to 2D
        res_grid = [[0] * m for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(m):
                res_grid[i][j] = result[idx]
                idx += 1
        
        return res_grid