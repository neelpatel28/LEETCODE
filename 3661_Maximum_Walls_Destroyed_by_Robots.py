from bisect import bisect_left, bisect_right

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        pairs = sorted(zip(robots, distance))
        robots = [p[0] for p in pairs]
        distance = [p[1] for p in pairs]
        walls.sort()
        
        n = len(robots)
        
        def count(l, r):
            return bisect_right(walls, r) - bisect_left(walls, l)
        
        # Step 1: compute intervals
        left_interval = []
        right_interval = []
        
        for i in range(n):
            pos = robots[i]
            dist = distance[i]
            
            # LEFT
            lb = robots[i-1] + 1 if i > 0 else -10**18
            L = max(pos - dist, lb)
            R = pos
            left_interval.append((L, R))
            
            # RIGHT
            rb = robots[i+1] - 1 if i < n-1 else 10**18
            L = pos
            R = min(pos + dist, rb)
            right_interval.append((L, R))
        
        # Step 2: counts
        left_cnt = [0]*n
        right_cnt = [0]*n
        
        for i in range(n):
            L, R = left_interval[i]
            if L <= R:
                left_cnt[i] = count(L, R)
            
            L, R = right_interval[i]
            if L <= R:
                right_cnt[i] = count(L, R)
        
        # Step 3: overlap
        overlap = [0]*n
        
        for i in range(1, n):
            L1, R1 = right_interval[i-1]
            L2, R2 = left_interval[i]
            
            L = max(L1, L2)
            R = min(R1, R2)
            
            if L <= R:
                overlap[i] = count(L, R)
        
        # Step 4: DP
        dp0 = left_cnt[0]
        dp1 = right_cnt[0]
        
        for i in range(1, n):
            new_dp0 = max(
                dp0 + left_cnt[i],
                dp1 + left_cnt[i] - overlap[i]
            )
            
            new_dp1 = max(
                dp1 + right_cnt[i],
                dp0 + right_cnt[i]
            )
            
            dp0, dp1 = new_dp0, new_dp1
        
        return max(dp0, dp1)