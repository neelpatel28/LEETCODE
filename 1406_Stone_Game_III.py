class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # Allocate space for n + 3 elements to comfortably avoid out-of-bounds errors
        dp = [0] * (n + 3)
        
        # Traverse backward from the end of the array
        for i in range(n - 1, -1, -1):
            current_take = 0
            max_relative_score = float('-inf')
            
            # A player can pick 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    current_take += stoneValue[i + k - 1]
                    max_relative_score = max(max_relative_score, current_take - dp[i + k])
            
            dp[i] = max_relative_score
            
        # Determine the winner based on Alice's first-turn relative advantage
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
