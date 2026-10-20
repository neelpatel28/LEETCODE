class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            is_valid_k = True
            prev_max = float('-inf')

            for i in range(0, n, k):
                dips = 0
                block_min = nums[i]
                block_max = nums[i]

                for j in range(i + 1, i + k):
                    if nums[j] < nums[j - 1]:
                        dips += 1
                    if nums[j] < block_min:
                        block_min = nums[j]
                    if nums[j] > block_max:
                        block_max = nums[j]

                if dips > 1 or (dips == 1 and nums[i + k - 1] > nums[i]):
                    is_valid_k = False
                    break

                if block_min < prev_max:
                    is_valid_k = False
                    break

                prev_max = block_max

            if is_valid_k:
                ans += k

        return ans
