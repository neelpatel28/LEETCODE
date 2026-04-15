class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                min_dist = min(min_dist, d, n - d)
        
        return -1 if min_dist == float('inf') else min_dist