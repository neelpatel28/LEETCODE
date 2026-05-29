class Solution(object):
    def minElement(self, nums):
        min_val = 46
        for num in nums:
            s = 0
            while num:
                s += num % 10
                num //= 10
                if s >= min_val:
                    break
            if s < min_val:
                min_val = s
                if min_val == 1:
                    return 1
        return min_val