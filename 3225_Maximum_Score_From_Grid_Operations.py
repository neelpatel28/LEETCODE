class Solution(object):
    def maximumScore(self, grid):
        n = len(grid)
        NEG_INF = float('-inf')
        
        # prefix[j][i] = sum of grid[0][j] .. grid[i-1][j]
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i+1] = prefix[j][i] + grid[i][j]
        
        # dp[prev_h][cur_h]: max score with col j-1 cutoff=prev_h, col j cutoff=cur_h
        # col j's whites not yet counted; initialize at col 0 with virtual prev col cutoff=0
        dp = [[NEG_INF] * (n + 1) for _ in range(n + 1)]
        for cur_h in range(n + 1):
            dp[0][cur_h] = 0
        
        for j in range(1, n):
            P = prefix[j - 1]
            new_dp = [[NEG_INF] * (n + 1) for _ in range(n + 1)]
            
            for cur_h in range(n + 1):
                # prefix max: pre_max[v] = max over prev_h in [0..v] of dp[prev_h][cur_h]
                pre_max = [NEG_INF] * (n + 1)
                pre_max[0] = dp[0][cur_h]
                for v in range(1, n + 1):
                    pre_max[v] = max(pre_max[v - 1], dp[v][cur_h])
                
                # suffix max of dp[prev_h][cur_h] + max(0, P[prev_h] - P[cur_h])
                suf_g = [NEG_INF] * (n + 2)
                for v in range(n, -1, -1):
                    d = dp[v][cur_h]
                    g = d + max(0, P[v] - P[cur_h]) if d != NEG_INF else NEG_INF
                    suf_g[v] = max(suf_g[v + 1], g)
                
                for nxt_h in range(n + 1):
                    # Case A: prev_h <= nxt_h → gain = max(0, P[nxt_h] - P[cur_h])
                    caseA = (pre_max[nxt_h] + max(0, P[nxt_h] - P[cur_h])
                             if pre_max[nxt_h] != NEG_INF else NEG_INF)
                    # Case B: prev_h > nxt_h → gain = max(0, P[prev_h] - P[cur_h])
                    caseB = suf_g[nxt_h + 1]
                    new_dp[cur_h][nxt_h] = max(caseA, caseB)
            
            dp = new_dp
        
        # Score last column's whites: virtual right neighbor has cutoff 0
        ans = 0
        P = prefix[n - 1]
        for prev_h in range(n + 1):
            for cur_h in range(n + 1):
                if dp[prev_h][cur_h] != NEG_INF:
                    gain = max(0, P[prev_h] - P[cur_h])  # nxt_h=0, max(prev_h,0)=prev_h
                    ans = max(ans, dp[prev_h][cur_h] + gain)
        return ans