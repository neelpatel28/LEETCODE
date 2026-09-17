class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        prefix_sums = {0: -1}
        current_sum = 0
        n = len(arr)
        
        min_len = [float('inf')] * n
        min_total_length = float('inf')
        best_till_now = float('inf')
        
        for r in range(n):
            current_sum += arr[r]
            needed_sum = current_sum - target
            
            if needed_sum in prefix_sums:
                l = prefix_sums[needed_sum]
                current_len = r - l
                
                if l >= 0 and min_len[l] != float('inf'):
                    min_total_length = min(min_total_length, current_len + min_len[l])
                
                best_till_now = min(best_till_now, current_len)
            
            min_len[r] = best_till_now
            prefix_sums[current_sum] = r

        return min_total_length if min_total_length != float('inf') else -1
