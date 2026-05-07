class Solution:
    def maxValue(self, nums):
        n = len(nums)

        ans = [0] * n

        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            if nums[i] > pre_max[i - 1]:
                pre_max[i] = nums[i]
            else:
                pre_max[i] = pre_max[i - 1]

        suf_min = float('inf')

        for i in range(n - 1, -1, -1):
            if i < n - 1 and pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]

            if nums[i] < suf_min:
                suf_min = nums[i]

        return ans