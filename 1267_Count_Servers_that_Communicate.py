class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        rows = [0] * m
        cols = [0] * n

        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0

        # Count communicating servers
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1

        return ans
