from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        dq = deque()
        n = len(nums)

        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            num = nums[left]
            count = 1

            # Merge smaller segments into the current segment
            while dq and dq[-1][0] < num:
                val, cnt = dq.pop()

                cost += (num - val) * cnt
                count += cnt

            dq.append((num, count))

            # Shrink the window while cost exceeds k
            while cost > k:
                val, cnt = dq[0]

                cost -= val - nums[right]

                if cnt == 1:
                    dq.popleft()
                else:
                    dq[0] = (val, cnt - 1)

                right -= 1

            # Count all valid subarrays ending within the window
            ans += right - left + 1

        return ans
