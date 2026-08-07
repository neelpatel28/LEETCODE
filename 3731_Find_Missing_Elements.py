class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        mn = min(nums)
        mx = max(nums)
        res = []
        for x in range(mn, mx + 1):
            if x not in s:
                res.append(x)
        return res
