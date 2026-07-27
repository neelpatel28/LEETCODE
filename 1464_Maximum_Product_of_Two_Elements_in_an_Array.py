class Solution(object):
    def maxProduct(self, nums):
        a = b = 0
        for x in nums:
            if x > a:
                a, b = x, a
            elif x > b:
                b = x
        return (a - 1) * (b - 1)