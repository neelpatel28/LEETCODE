from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        sorted_intervals = sorted((l, r, w, idx) for idx, (l, r, w) in enumerate(intervals))
        starts = [x[0] for x in sorted_intervals]
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            curr_l, curr_r, curr_w, curr_idx = sorted_intervals[i]
            nxt = bisect_left(starts, curr_r + 1)
            
            for count in range(1, 5):
                skip_w, skip_indices = dp[i + 1][count]
                
                take_w, take_indices = dp[nxt][count - 1]
                take_w += curr_w
                new_indices = tuple(sorted(take_indices + (curr_idx,)))
                
                if take_w > skip_w:
                    dp[i][count] = (take_w, new_indices)
                elif skip_w > take_w:
                    dp[i][count] = (skip_w, skip_indices)
                else:
                    if new_indices < skip_indices:
                        dp[i][count] = (take_w, new_indices)
                    else:
                        dp[i][count] = (skip_w, skip_indices)
                        
        return list(dp[0][4][1])
