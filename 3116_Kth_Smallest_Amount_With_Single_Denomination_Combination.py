import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        
        # 1. Precompute the Least Common Multiple (LCM) for all non-empty subsets
        for i in range(1, 1 << n):
            current_lcm = 1
            bits_set = 0
            for j in range(n):
                if (i >> j) & 1:
                    # Python 3.9+ supports math.lcm, but this is a safe universal alternative
                    current_lcm = (current_lcm * coins[j]) // math.gcd(current_lcm, coins[j])
                    bits_set += 1
            
            # Odd number of elements: add, Even number of elements: subtract
            sign = 1 if bits_set % 2 != 0 else -1
            subsets.append((current_lcm, sign))
            
        # 2. Helper function to count unique multiples <= mid via Inclusion-Exclusion
        def count_multiples(mid: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (mid // lcm_val)
            return total

        # 3. Binary search for the kth smallest value
        low = 1
        high = k * min(coins)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the lower boundary
                
        return ans
