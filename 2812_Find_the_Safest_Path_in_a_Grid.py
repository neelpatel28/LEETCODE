from collections import deque


class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        distance = [[-1] * n for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distance[i][j] = 0
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col
                if 0 <= next_row < n and 0 <= next_col < n and distance[next_row][next_col] == -1:
                    distance[next_row][next_col] = distance[row][col] + 1
                    queue.append((next_row, next_col))

        left, right = 0, n

        while left < right:
            mid = (left + right + 1) // 2
            if self._can_reach(grid, distance, mid):
                left = mid
            else:
                right = mid - 1

        return left

    def _can_reach(self, grid, distance, minimum_safety):
        n = len(grid)
        if distance[0][0] < minimum_safety or distance[n - 1][n - 1] < minimum_safety:
            return False

        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            if row == n - 1 and col == n - 1:
                return True

            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col
                if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                    if distance[next_row][next_col] >= minimum_safety:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))

        return False
