class Solution(object):
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            newDp = [0] * k
            numMod = num % k
            newDp[numMod] = 1
            
            for i in range(k):
                if dp[i] > 0:
                    newMod = (i * numMod) % k
                    newDp[newMod] += dp[i]
            
            for i in range(k):
                ans[i] += newDp[i]
                
            dp = newDp
            
        return ans
