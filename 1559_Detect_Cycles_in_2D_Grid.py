class Solution(object):
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        def dfs(r, c, pr, pc, char):
            if visited[r][c]:
                return True
            
            visited[r][c] = 1
            
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == char:
                    if nr == pr and nc == pc:
                        continue
                    
                    if dfs(nr, nc, r, c, char):
                        return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False