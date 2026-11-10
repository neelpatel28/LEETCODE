class Solution(object):
    def climbStairs(self, n, costs):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = min(
                dp[i - 1] + costs[i - 1] + 1,
                dp[i - 2] + costs[i - 1] + 4 if i >= 2 else float('inf'),
                dp[i - 3] + costs[i - 1] + 9 if i >= 3 else float('inf')
            )

        return dp[n]
