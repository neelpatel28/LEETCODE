class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        mod = 10**9 + 7
        dp_max = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        dp_max[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                best = -1
                count = 0
                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    ni = i + di
                    nj = j + dj
                    if ni < n and nj < n and dp_count[ni][nj] > 0:
                        candidate = dp_max[ni][nj]
                        if candidate > best:
                            best = candidate
                            count = dp_count[ni][nj]
                        elif candidate == best:
                            count = (count + dp_count[ni][nj]) % mod
                if count > 0:
                    cell_value = 0 if board[i][j] in 'SE' else ord(board[i][j]) - 48
                    dp_max[i][j] = best + cell_value
                    dp_count[i][j] = count
        if dp_count[0][0] == 0:
            return [0, 0]
        return [dp_max[0][0], dp_count[0][0]]
