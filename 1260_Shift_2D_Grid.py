class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        k %= m * n
        return [[grid[(i * n + j - k) // n % m][(i * n + j - k) % n] for j in range(n)] for i in range(m)]