import bisect

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        # Sort water rides by start time, precompute structures
        water = sorted(zip(waterStartTime, waterDuration), key=lambda x: x[0])
        water_starts = [w[0] for w in water]
        water_durs = [w[1] for w in water]
        
        # prefix_min_dur[i] = min waterDuration among water[0..i]
        m = len(water)
        prefix_min_dur_water = [0] * m
        prefix_min_dur_water[0] = water_durs[0]
        for i in range(1, m):
            prefix_min_dur_water[i] = min(prefix_min_dur_water[i-1], water_durs[i])
        
        # suffix_min_finish[i] = min (waterStart + waterDur) among water[i..m-1]
        suffix_min_finish_water = [0] * m
        suffix_min_finish_water[m-1] = water_starts[m-1] + water_durs[m-1]
        for i in range(m-2, -1, -1):
            suffix_min_finish_water[i] = min(suffix_min_finish_water[i+1], water_starts[i] + water_durs[i])
        
        # Same for land rides
        land = sorted(zip(landStartTime, landDuration), key=lambda x: x[0])
        land_starts = [l[0] for l in land]
        land_durs = [l[1] for l in land]
        n = len(land)
        
        prefix_min_dur_land = [0] * n
        prefix_min_dur_land[0] = land_durs[0]
        for i in range(1, n):
            prefix_min_dur_land[i] = min(prefix_min_dur_land[i-1], land_durs[i])
        
        suffix_min_finish_land = [0] * n
        suffix_min_finish_land[n-1] = land_starts[n-1] + land_durs[n-1]
        for i in range(n-2, -1, -1):
            suffix_min_finish_land[i] = min(suffix_min_finish_land[i+1], land_starts[i] + land_durs[i])
        
        def best_water_after(t):
            # min finish time for a water ride started >= t
            # case 1: waterStart[j] >= t → use suffix_min_finish
            idx = bisect.bisect_left(water_starts, t)
            res = float('inf')
            if idx < m:
                res = min(res, suffix_min_finish_water[idx])
            # case 2: waterStart[j] < t → finish = t + waterDur[j], minimize waterDur
            if idx > 0:
                res = min(res, t + prefix_min_dur_water[idx-1])
            return res
        
        def best_land_after(t):
            idx = bisect.bisect_left(land_starts, t)
            res = float('inf')
            if idx < n:
                res = min(res, suffix_min_finish_land[idx])
            if idx > 0:
                res = min(res, t + prefix_min_dur_land[idx-1])
            return res
        
        ans = float('inf')
        
        # Land first, then water
        for i in range(len(landStartTime)):
            t = landStartTime[i] + landDuration[i]
            ans = min(ans, best_water_after(t))
        
        # Water first, then land
        for j in range(len(waterStartTime)):
            t = waterStartTime[j] + waterDuration[j]
            ans = min(ans, best_land_after(t))
        
        return ans