class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                ans += len(seen) ** 2

        return ans
