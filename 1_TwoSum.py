class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            
# Logic : It is two sum so for each number we will check if the complement (target - current number) is already seen in the dictionary. If it is, we return the indices of the complement and the current number. If not, we add the current number and its index to the dictionary for future reference.
sol = Solution()

# nums = [2, 7, 11, 15] 
# target = 9
# # ans : [0, 1]

# nums = [3, 2, 4]
# target = 7
# # ans : [1,2]


nums = [3, 1, 8, 6, 2, 4, 5]
target = 14
# # ans : [2, 3]

result = sol.twoSum(nums, target)
print(result)