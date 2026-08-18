class Solution:
    def largestInteger(self, nums: List, k):
        from collections import Counter
        
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: k == 1
        if k == 1:
            ans = -1
            for num, freq in counts.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 2: k == n
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
