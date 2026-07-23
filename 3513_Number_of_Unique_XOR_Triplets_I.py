class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        b = n.bit_length()
        return 1 << b