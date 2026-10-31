
class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(grid[0])

        dp = [1] + [0] * (n - 1)

        for row in grid:
            left = 0

            for j in range(n):
                if row[j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left
