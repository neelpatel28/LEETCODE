class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.comp = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        self.comp -= 1
        return True


class Solution(object):
    def maxStability(self, n, edges, k):

        def can(x):
            dsu = DSU(n)
            upgrades = 0
            used = 0

            # mandatory edges
            for u, v, s, m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False
                    used += 1

            normal = []
            upgrade = []

            for u, v, s, m in edges:
                if m == 0:
                    if s >= x:
                        normal.append((u, v))
                    elif 2*s >= x:
                        upgrade.append((u, v))

            for u, v in normal:
                if dsu.union(u, v):
                    used += 1

            for u, v in upgrade:
                if used == n-1:
                    break
                if dsu.union(u, v):
                    upgrades += 1
                    used += 1
                    if upgrades > k:
                        return False

            return used == n-1

        lo, hi = 0, 2*10**5
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans