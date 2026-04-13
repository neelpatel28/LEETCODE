class Solution(object):    
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(min_dist, abs(i - start))
        
        return min_dist
    
    
obj = Solution()

print(obj.getMinDistance([1, 2, 3, 4, 5], 5, 3))  # Output: 1
print(obj.getMinDistance([1], 1, 0))  # Output: 0
print(obj.getMinDistance([1, 1, 1, 1, 1], 1, 0))  # Output: 0
print(obj.getMinDistance([1, 2, 3, 4, 5], 6, 3))  # Output: inf (target not found)