from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter_id = [[-1] * n for _ in range(m)]
        start_r = start_c = 0
        litter_count = 0

        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]

                if cell == 'S':
                    start_r = r
                    start_c = c
                elif cell == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1
        mask_count = 1 << litter_count

        best = [
            [-1] * (n * mask_count)
            for _ in range(m)
        ]

        start_index = (start_c * mask_count) + full_mask
        best[start_r][start_index] = energy

        queue = deque()
        queue.append((start_r, start_c, energy, full_mask))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, current_energy, mask = queue.popleft()

                if mask == 0:
                    return moves

                if current_energy == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    cell = classroom[nr][nc]

                    if cell == 'X':
                        continue

                    next_energy = current_energy - 1
                    next_mask = mask

                    if cell == 'R':
                        next_energy = energy

                    elif cell == 'L':
                        next_mask &= ~(1 << litter_id[nr][nc])

                    index = nc * mask_count + next_mask

                    if next_energy <= best[nr][index]:
                        continue

                    best[nr][index] = next_energy
                    queue.append((nr, nc, next_energy, next_mask))

            moves += 1

        return -1
