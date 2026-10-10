class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        
        max_diff = 0
        diff_counts = [0] * 100001
        
        for n1, n2 in zip(nums1, nums2):
            d = abs(n1 - n2)
            if d > 0:
                diff_counts[d] += 1
                if d > max_diff:
                    max_diff = d
                    
        if sum(d * count for d, count in enumerate(diff_counts)) <= k:
            return 0
            
        for d in range(max_diff, 0, -1):
            if diff_counts[d] == 0:
                continue
                
            take = min(k, diff_counts[d])
            
            diff_counts[d] -= take
            diff_counts[d - 1] += take
            k -= take
            
            if k == 0:
                break
                
        return sum(count * (d ** 2) for d, count in enumerate(diff_counts))
