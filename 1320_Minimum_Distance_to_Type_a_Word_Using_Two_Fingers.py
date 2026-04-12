class Solution:
    def minimumDistance(self, word):
        def dist(a, b):
            if a == 26:  # unused finger
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        # convert chars to indices 0–25
        w = [ord(c) - ord('A') for c in word]

        # dp[j] = min cost where other finger is at j
        dp = [float('inf')] * 27
        dp[26] = 0  # initially other finger unused

        for i in range(n - 1):
            new_dp = [float('inf')] * 27
            for j in range(27):
                if dp[j] == float('inf'):
                    continue
                
                # Option 1: same finger types next char
                cost1 = dp[j] + dist(w[i], w[i + 1])
                new_dp[j] = min(new_dp[j], cost1)
                
                # Option 2: other finger types next char
                cost2 = dp[j] + dist(j, w[i + 1])
                new_dp[w[i]] = min(new_dp[w[i]], cost2)
            
            dp = new_dp

        return min(dp)