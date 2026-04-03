class Solution(object):
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                res.add(grid[r][c])  # k = 0 rhombus
                
                k = 1
                while r-k >= 0 and r+k < m and c-k >= 0 and c+k < n:
                    total = 0

                    # top -> right
                    for d in range(k):
                        total += grid[r-k+d][c+d]

                    # right -> bottom
                    for d in range(k):
                        total += grid[r+d][c+k-d]

                    # bottom -> left
                    for d in range(k):
                        total += grid[r+k-d][c-d]

                    # left -> top
                    for d in range(k):
                        total += grid[r-d][c-k+d]

                    res.add(total)
                    k += 1

        return sorted(res, reverse=True)[:3]