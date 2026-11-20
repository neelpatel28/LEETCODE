class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()

        ans = 1
        prev = nums[0]

        # dp0: Best sequence ending at prev
        # dp1: Best sequence ending at prev + 1
        dp0 = 1
        dp1 = 1

        for num in nums[1:]:
            if num == prev:
                # Use current element as prev + 1
                dp1 = dp0 + 1

            elif num == prev + 1:
                # Extend both possible sequences
                dp0 += 1
                dp1 += 1

            elif num == prev + 2:
                # Extend dp1 using the current unmodified value
                dp0 = dp1 + 1
                dp1 = 1

            else:
                # Gap is too large; start new sequences
                dp0 = 1
                dp1 = 1

            ans = max(ans, dp0, dp1)
            prev = num

        return ans
