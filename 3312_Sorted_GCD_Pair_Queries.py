import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        
        count = [0] * (max_val + 1)
        
        for g in range(1, max_val + 1):
            total = 0
            for m in range(g, max_val + 1, g):
                total += freq[m]
            count[g] = total * (total - 1) // 2
        
        for g in range(max_val, 0, -1):
            for m in range(2 * g, max_val + 1, g):
                count[g] -= count[m]
        
        prefix = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            prefix[g] = prefix[g - 1] + count[g]
        
        res = []
        for q in queries:
            g = bisect.bisect_right(prefix, q)
            res.append(g)
        
        return res