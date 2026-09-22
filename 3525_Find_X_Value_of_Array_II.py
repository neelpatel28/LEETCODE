class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right
            res_prod = (left_prod * right_prod) % k
            res_cnt = list(left_cnt)
            for r in range(k):
                if right_cnt[r] > 0:
                    new_rem = (left_prod * r) % k
                    res_cnt[new_rem] += right_cnt[r]
            return [res_prod, res_cnt]

        def build(node, start, end):
            if start == end:
                val = nums[start] % k
                cnt = [0] * k
                cnt[val] = 1
                tree[node] = [val, cnt]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, val):
            if start == end:
                v = val % k
                cnt = [0] * k
                cnt[v] = 1
                tree[node] = [v, cnt]
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def query(node, start, end, l, r):
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            if l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            left_res = query(2 * node, start, mid, l, r)
            right_res = query(2 * node + 1, mid + 1, end, l, r)
            return merge(left_res, right_res)

        build(1, 0, n - 1)
        ans = []
        for index_i, value_i, start_i, x_i in queries:
            update(1, 0, n - 1, index_i, value_i)
            _, res_cnt = query(1, 0, n - 1, start_i, n - 1)
            ans.append(res_cnt[x_i])
        return ans
