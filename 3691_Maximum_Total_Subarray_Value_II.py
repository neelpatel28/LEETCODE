import heapq
import math


class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or k == 0:
            return 0

        # precompute logs
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        K = log[n] + 1
        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = 1 << (j - 1)
            for i in range(0, n - length + 1):
                st_max[j][i] = st_max[j - 1][i] if st_max[j - 1][i] >= st_max[j - 1][i + half] else st_max[j - 1][i + half]
                st_min[j][i] = st_min[j - 1][i] if st_min[j - 1][i] <= st_min[j - 1][i + half] else st_min[j - 1][i + half]
            j += 1

        def range_max(l, r):
            j = log[r - l + 1]
            a = st_max[j][l]
            b = st_max[j][r - (1 << j) + 1]
            return a if a >= b else b

        def range_min(l, r):
            j = log[r - l + 1]
            a = st_min[j][l]
            b = st_min[j][r - (1 << j) + 1]
            return a if a <= b else b

        def v(l, r):
            return range_max(l, r) - range_min(l, r)

        # max-heap using negative values, initial entries (l, n-1)
        heap = []
        for l in range(n):
            val = v(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        ans = 0
        times = min(k, n * (n + 1) // 2)
        while times > 0 and heap:
            negval, l, r = heapq.heappop(heap)
            ans += -negval
            times -= 1
            if r > l:
                nr = r - 1
                nval = v(l, nr)
                heapq.heappush(heap, (-nval, l, nr))

        return ans


if __name__ == "__main__":
    # simple smoke tests
    s = Solution()
    print(s.maxTotalValue([1, 3, 2], 2))  # expect 4
    print(s.maxTotalValue([4, 2, 5, 1], 3))  # expect 12
