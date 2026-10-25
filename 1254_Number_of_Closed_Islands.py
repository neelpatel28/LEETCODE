class Solution:
  def closedIsland(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def dfs(i: int, j: int) -> None:
      if i < 0 or i == m or j < 0 or j == n:
        return
      if grid[i][j] == 1:
        return
      grid[i][j] = 1
      dfs(i + 1, j)
      dfs(i - 1, j)
      dfs(i, j + 1)
      dfs(i, j - 1)

    # Step 1: Eliminate any land cells (0) connected to the grid boundary
    for i in range(m):
      for j in range(n):
        if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 0:
          dfs(i, j)

    # Step 2: Count remaining isolated land components
    ans = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          dfs(i, j)
          ans += 1

    return ans
