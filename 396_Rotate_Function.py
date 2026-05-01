# method 1 

class Solution(object):
    def maxRotateFunction(self,nums):
        sums = []
        for k in range(len(nums)):
            sum = 0
            rotated = nums[-k:] + nums[:-k]
            # print(k+1, " : ",rotated)
            for i in range(len(rotated)):
                sum += i*rotated[i]
            sums.append(sum)
            # print(k+1, " : ",sum)
        # print(f"\nAnswer : {max(sums)}")
        return max(sums)
          
          
          
          
            
# method 2 {OPTIMIZED}

class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        F = 0
        for i in range(n):
            F += i * nums[i]
        
        max_val = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)
        
        return max_val