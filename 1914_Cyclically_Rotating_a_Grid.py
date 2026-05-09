class Solution(object):
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for layer in range(layers):
            elems = []
            
            top, bottom = layer, m - layer - 1
            left, right = layer, n - layer - 1
            
            for j in range(left, right + 1):
                elems.append(grid[top][j])
            
            for i in range(top + 1, bottom):
                elems.append(grid[i][right])
            
            for j in range(right, left - 1, -1):
                elems.append(grid[bottom][j])
            
            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])
            
            k_mod = k % len(elems)
            rotated = elems[k_mod:] + elems[:k_mod]
            
            idx = 0
            
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1
            
            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            
            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
        
        return grid