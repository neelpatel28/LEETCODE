class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Directions: (dr, dc)
        dirs = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        
        # Reverse direction mapping
        def is_connected(from_r, from_c, to_r, to_c):
            dr, dc = to_r - from_r, to_c - from_c
            # reverse direction must exist in next cell
            return (-dr, -dc) in dirs[grid[to_r][to_c]]
        
        visited = [[False] * n for _ in range(m)]
        
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True
            
            visited[r][c] = True
            
            for dr, dc in dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if is_connected(r, c, nr, nc):
                        if dfs(nr, nc):
                            return True
            
            return False
        
        return dfs(0, 0)