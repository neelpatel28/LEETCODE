class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i, x in enumerate(nums):
            if x == target:
                res.append(i)
        return res
