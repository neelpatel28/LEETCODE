class Solution(object):
    def findDifferentBinaryString(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return "".join(res)

# Logic : We can construct a binary string by flipping the i-th bit of the i-th string in the input list. 
# This way, we ensure that the constructed string is different from every string in the input list at least at one position.
sol = Solution()

nums = ["1"] # Output: "0"
# nums = ["01","10"] # Output: "11"
# nums = ["001","010","111"] # Output: "100"
# nums = ["0111","1011","1001","0000"] # Output: "1111"

result = sol.findDifferentBinaryString(nums)

print(result)