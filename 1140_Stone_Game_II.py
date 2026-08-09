class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        
        # Calculate suffix sums for quick remainder calculation
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i, M):
            # No piles left
            if i >= n:
                return 0
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            # Return cached result
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            # Try taking X piles
            for X in range(1, 2 * M + 1):
                opponent_stones = dfs(i + X, max(M, X))
                current_stones = suffix_sum[i] - opponent_stones
                max_stones = max(max_stones, current_stones)
                
            memo[(i, M)] = max_stones
            return max_stones
            
        return dfs(0, 1)
