
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        ans = 0

        for i, x in enumerate(nums):
            if i < n // 2:
                ans -= x * x
            else:
                ans += x * x

        return ans
