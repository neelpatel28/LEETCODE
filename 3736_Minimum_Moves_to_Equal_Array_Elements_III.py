class Solution(object):
    def minMoves(self, nums):
        mx = max(nums)
        return mx * len(nums) - sum(nums)
