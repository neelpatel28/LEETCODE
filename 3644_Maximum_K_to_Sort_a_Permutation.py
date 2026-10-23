class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
        
        # If ans remains -1, the array was already sorted, so return 0
        return max(ans, 0)
