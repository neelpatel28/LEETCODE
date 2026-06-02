class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)
        
        ans = float('inf')
        
        for i in range(n):
            for j in range(m):
                
                # Case 1: Land -> Water
                end_land = landStartTime[i] + landDuration[i]
                start_water = max(end_land, waterStartTime[j])
                finish1 = start_water + waterDuration[j]
                
                # Case 2: Water -> Land
                end_water = waterStartTime[j] + waterDuration[j]
                start_land = max(end_water, landStartTime[i])
                finish2 = start_land + landDuration[i]
                
                ans = min(ans, finish1, finish2)
        
        return ans