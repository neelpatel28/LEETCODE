class Solution(object):
    def isGood(self, nums):
        n = max(nums)
        
        if len(nums) != n + 1:
            return False
        
        freq = [0] * (n + 1)
        
        for num in nums:
            if num > n or num < 1:
                return False
            freq[num] += 1
        
        for i in range(1, n):
            if freq[i] != 1:
                return False
        
        if freq[n] != 2:
            return False
        
        return True