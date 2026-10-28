class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Initialize a 2D grid where each cell contains a set of reachable XOR sums
        dp = [[set() for _ in range(COLS)] for _ in range(ROWS)]
        
        # Base case: the starting cell
        dp[0][0].add(grid[0][0])
        
        # Populate the DP table row by row, column by column
        for r in range(ROWS):
            for c in range(COLS):
                # If we can come from the left neighbor
                if c > 0:
                    for prev_xor in dp[r][c-1]:
                        dp[r][c].add(prev_xor ^ grid[r][c])
                        
                # If we can come from the top neighbor
                if r > 0:
                    for prev_xor in dp[r-1][c]:
                        dp[r][c].add(prev_xor ^ grid[r][c])
        
        # The answer is the absolute minimum XOR value found at the bottom-right corner
        return min(dp[ROWS-1][COLS-1])
