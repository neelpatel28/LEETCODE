class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        return sum(num - minimum for num in nums)
