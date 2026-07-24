class Solution(object):
    def uniqueXorTriplets(self, nums):
        S = set(nums)
        
        pair = set()
        for x in S:
            for y in S:
                pair.add(x ^ y)
        
        res = set()
        for p in pair:
            for z in S:
                res.add(p ^ z)
        
        return len(res)