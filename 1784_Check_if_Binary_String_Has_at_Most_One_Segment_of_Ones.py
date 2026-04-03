class Solution(object):
    def checkOnesSegment(self, s):
        ans = True
        found_0 = False
        for i in range(len(s)):
            if s[i] == "0":
                found_0 = True
            elif s[i] == "1" and found_0:
                ans = False
                break

        return ans

sol = Solution()
# s = '1' # Output: True
# s = "11" # Output: True
s = "001" # Output: False
# s = "101" # Output: False
# s = "110" # Output: True

result = sol.checkOnesSegment(s)

print(result)