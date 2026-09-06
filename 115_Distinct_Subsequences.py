class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        # dp[j] stores the number of subsequences matching t[0...j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string t can always be formed in 1 way
        
        for char_s in s:
            # Iterate backwards to avoid using updated values from the same row
            for j in range(n, 0, -1):
                if char_s == t[j-1]:
                    dp[j] += dp[j-1]
                    
        return dp[n]
