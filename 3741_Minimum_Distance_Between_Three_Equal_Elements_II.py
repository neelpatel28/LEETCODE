class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # Store indices of each value
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = float('inf')
        
        # Process each value
        for indices in pos.values():
            if len(indices) >= 3:
                # Check all triplets of consecutive indices
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i + 2] - indices[i])
                    ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1