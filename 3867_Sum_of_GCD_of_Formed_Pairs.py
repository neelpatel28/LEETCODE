class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0] * n
        
        mx = 0
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd[i] = self.gcd(nums[i], mx)
        
        prefixGcd.sort()
        
        l, r = 0, n - 1
        ans = 0
        
        while l < r:
            ans += self.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        
        return ans