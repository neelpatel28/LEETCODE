class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, start, end):
            if lazy[node] == 0:
                return
            val = lazy[node]
            lazy[node] = 0
            
            mid = (start + end) // 2
            left, right = 2 * node, 2 * node + 1
            
            lazy[left] = (lazy[left] + val) % MOD
            lazy[right] = (lazy[right] + val) % MOD
            
            tree_sq[left] = (tree_sq[left] + 2 * val * tree_sum[left] + val * val * (mid - start + 1)) % MOD
            tree_sum[left] = (tree_sum[left] + val * (mid - start + 1)) % MOD
            
            tree_sq[right] = (tree_sq[right] + 2 * val * tree_sum[right] + val * val * (end - mid)) % MOD
            tree_sum[right] = (tree_sum[right] + val * (end - mid)) % MOD

        def update(node, start, end, l, r, val):
            if start > end or start > r or end < l:
                return
            if start >= l and end <= r:
                tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * (end - start + 1)) % MOD
                tree_sum[node] = (tree_sum[node] + val * (end - start + 1)) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        total_ans = 0
        last_pos = {}
        
        for i, num in enumerate(nums):
            j = last_pos.get(num, -1)
            update(1, 0, n - 1, j + 1, i, 1)
            total_ans = (total_ans + tree_sq[1]) % MOD
            last_pos[num] = i
            
        return total_ans
