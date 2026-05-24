class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * n
        
        order = list(range(n))
        order.sort(key=arr.__getitem__)
        
        for i in order:
            ai = arr[i]
            dpi = dp[i]
            
            j = i - 1
            limit = max(0, i - d)
            while j >= limit:
                if arr[j] >= ai:
                    break
                if dp[j] + 1 > dpi:
                    dpi = dp[j] + 1
                j -= 1
            
            j = i + 1
            limit = min(n, i + d + 1)
            while j < limit:
                if arr[j] >= ai:
                    break
                if dp[j] + 1 > dpi:
                    dpi = dp[j] + 1
                j += 1
            
            dp[i] = dpi
        
        return max(dp)