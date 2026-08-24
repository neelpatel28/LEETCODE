class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]
        
        res = stones[-1]
        for i in range(n - 2, 0, -1):
            res = max(res, stones[i] - res)
        return res
