import math

class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            ways = comb(len(left) + len(right), len(left))
            
            return (ways * dfs(left) * dfs(right)) % MOD
            
        return (dfs(nums) - 1) % MOD
