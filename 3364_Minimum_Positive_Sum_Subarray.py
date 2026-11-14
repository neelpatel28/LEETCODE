class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        for i in range(n):
            for length in range(l, r + 1):
                j = i + length

                if j > n:
                    break

                total = prefix[j] - prefix[i]

                if 0 < total < ans:
                    ans = total

        return ans if ans != float('inf') else -1
