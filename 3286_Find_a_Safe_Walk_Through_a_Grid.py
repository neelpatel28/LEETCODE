from collections import deque


class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        start_health = health - grid[0][0]

        if start_health <= 0:
            return False

        q = deque([(0, 0, start_health)])
        visited = {(0, 0, start_health)}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, current_health = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_health = current_health - grid[nr][nc]
                    state = (nr, nc, next_health)
                    if next_health > 0 and state not in visited:
                        visited.add(state)
                        q.append(state)

        return False
