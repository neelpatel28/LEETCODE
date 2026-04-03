class Solution(object):
    def minFlips(self, s):
        n = len(s)
        s = s * 2
        res = float('inf')
        diff1 = diff2 = l = 0
        for r in range(len(s)):
            if s[r] != ('0' if r % 2 == 0 else '1'):
                diff1 += 1
            if s[r] != ('1' if r % 2 == 0 else '0'):
                diff2 += 1
            if r - l + 1 > n:
                if s[l] != ('0' if l % 2 == 0 else '1'):
                    diff1 -= 1
                if s[l] != ('1' if l % 2 == 0 else '0'):
                    diff2 -= 1
                l += 1
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        return res
    
# Logic : We can shift the string to left or right, so we can consider both cases by comparing with two alternating patterns. 
# We use a sliding window of size n to count the number of flips needed for both patterns and update the result accordingly.
sol = Solution()
#s = "1" # Output: 0
# s = "11" # Output: 1
# s = "001" # Output: 0, Explanation: The string is already alternating if we shift it to left once('010'), no flips are needed.
s = "01011" # Output: 0, Explanation: The string is already alternating if we shift it to right once('10101'), no flips are needed
# s = "111000" # Output: 2
result = sol.minFlips(s)

print(result)