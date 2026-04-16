class Solution(object):
    def solveQueries(self, nums, queries):
        from collections import defaultdict
        
        n = len(nums)
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = [-1] * n
        
        for v in pos:
            indices = pos[v]
            k = len(indices)
            
            if k == 1:
                continue
            
            for i in range(k):
                curr = indices[i]
                prev = indices[(i - 1) % k]
                nxt = indices[(i + 1) % k]
                
                d1 = abs(curr - prev)
                d1 = min(d1, n - d1)
                
                d2 = abs(curr - nxt)
                d2 = min(d2, n - d2)
                
                res[curr] = min(d1, d2)
        
        return [res[q] for q in queries]