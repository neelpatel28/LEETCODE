from collections import Counter

class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        # ---------- Horizontal Cuts ----------
        top_counter = Counter()
        bottom_counter = Counter()

        for r in range(m):
            for c in range(n):
                bottom_counter[grid[r][c]] += 1

        top_sum = 0

        for i in range(m - 1):
            row_sum = 0

            # move row i from bottom -> top
            for val in grid[i]:
                row_sum += val
                top_counter[val] += 1
                bottom_counter[val] -= 1
                if bottom_counter[val] == 0:
                    del bottom_counter[val]

            top_sum += row_sum
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # check heavier side
            if top_sum > bottom_sum:
                if diff in top_counter:
                    height = i + 1
                    width = n

                    if height > 1 and width > 1:
                        return True

                    # single row
                    if height == 1:
                        if grid[0][0] == diff or grid[0][width - 1] == diff:
                            return True

                    # single column
                    if width == 1:
                        if grid[0][0] == diff or grid[height - 1][0] == diff:
                            return True

            else:
                if diff in bottom_counter:
                    height = m - (i + 1)
                    width = n

                    if height > 1 and width > 1:
                        return True

                    # single row
                    if height == 1:
                        row = grid[i + 1]
                        if row[0] == diff or row[width - 1] == diff:
                            return True

                    # single column
                    if width == 1:
                        if grid[i + 1][0] == diff or grid[m - 1][0] == diff:
                            return True

        # ---------- Vertical Cuts ----------
        left_counter = Counter()
        right_counter = Counter()

        for r in range(m):
            for c in range(n):
                right_counter[grid[r][c]] += 1

        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]

        left_sum = 0

        for j in range(n - 1):
            # move column j from right -> left
            for r in range(m):
                val = grid[r][j]
                left_counter[val] += 1
                right_counter[val] -= 1
                if right_counter[val] == 0:
                    del right_counter[val]

            left_sum += col_sums[j]
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if diff in left_counter:
                    height = m
                    width = j + 1

                    if height > 1 and width > 1:
                        return True

                    # single row
                    if height == 1:
                        if grid[0][0] == diff or grid[0][width - 1] == diff:
                            return True

                    # single column
                    if width == 1:
                        if grid[0][0] == diff or grid[m - 1][0] == diff:
                            return True

            else:
                if diff in right_counter:
                    height = m
                    width = n - (j + 1)

                    if height > 1 and width > 1:
                        return True

                    # single row
                    if height == 1:
                        col_start = j + 1
                        if grid[0][col_start] == diff or grid[0][n - 1] == diff:
                            return True

                    # single column
                    if width == 1:
                        col = j + 1
                        if grid[0][col] == diff or grid[m - 1][col] == diff:
                            return True

        return False