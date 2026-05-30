class FenwickTree:
    def __init__(self, n):
        self.vals = [0] * (n + 1)

    def maximize(self, i, val):
        while i < len(self.vals):
            if self.vals[i] < val:
                self.vals[i] = val
            i += i & -i

    def get(self, i):
        res = 0
        while i > 0:
            if self.vals[i] > res:
                res = self.vals[i]
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        n = min(50000, len(queries) * 3)

        obstacles = [0, n]

        def bisect_left(arr, x):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m
            return l

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = bisect_left(obstacles, x)
                obstacles.insert(i, x)

        tree = FenwickTree(n + 1)

        for i in range(1, len(obstacles)):
            tree.maximize(obstacles[i], obstacles[i] - obstacles[i - 1])

        ans = []

        for qi in range(len(queries) - 1, -1, -1):
            q = queries[qi]

            if q[0] == 1:
                x = q[1]
                i = bisect_left(obstacles, x)
                prev = obstacles[i - 1]
                next = obstacles[i + 1]
                obstacles.pop(i)
                tree.maximize(next, next - prev)

            else:
                x, sz = q[1], q[2]
                i = bisect_left(obstacles, x + 1)
                prev = obstacles[i - 1]
                ans.append(tree.get(prev) >= sz or x - prev >= sz)

        return ans[::-1]