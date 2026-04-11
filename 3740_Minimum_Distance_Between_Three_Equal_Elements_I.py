class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        # Step 1: store indices for each number
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        
        min_dist = float('inf')
        
        # Step 2: process each value
        for indices in positions.values():
            if len(indices) >= 3:
                # Step 3: check all triplets (optimized to consecutive triplets)
                for i in range(len(indices) - 2):
                    left = indices[i]
                    right = indices[i + 2]
                    dist = 2 * (right - left)
                    min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1