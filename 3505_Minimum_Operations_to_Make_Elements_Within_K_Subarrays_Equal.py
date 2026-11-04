class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        count_bit = Fenwick(m)
        sum_bit = Fenwick(m)

        total_sum = 0

        def add(v, delta):
            nonlocal total_sum

            idx = pos[v]
            count_bit.update(idx, delta)
            sum_bit.update(idx, v * delta)
            total_sum += v * delta

        def get_cost():
            mid_idx = count_bit.kth((x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = count_bit.query(mid_idx)
            left_sum = sum_bit.query(mid_idx)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        # Calculate minimum cost for every window of size x.
        costs = []

        for i in range(x):
            add(nums[i], 1)

        costs.append(get_cost())

        for i in range(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)
            costs.append(get_cost())

        # DP: choose exactly k non-overlapping windows.
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    cost = costs[i - x]

                    if prev[i - x] != INF:
                        curr[i] = min(
                            curr[i],
                            prev[i - x] + cost
                        )

            prev = curr

        return prev[n]
