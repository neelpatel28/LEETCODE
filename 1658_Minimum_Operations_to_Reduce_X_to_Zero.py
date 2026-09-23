class Solution(object):
    def minOperations(self, nums, x):
        """:type nums: List[int]

        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        
        l, r, window_sum, max_len = 0, 0, 0, -1
        while r < len(nums):
            window_sum += nums[r]
            r += 1
            while window_sum > target and l < r:
                window_sum -= nums[l]
                l += 1
            if window_sum == target:
                max_len = max(max_len, r - l)
                
        return -1 if max_len == -1 else len(nums) - max_len
