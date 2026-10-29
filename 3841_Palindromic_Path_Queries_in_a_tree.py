class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOGN = (n - 1).bit_length()
        if LOGN == 0: 
            LOGN = 1
            
        up = [[0] * LOGN for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        path_mask = [0] * n

        masks = [1 << (ord(c) - ord('a')) for c in s]
        path_mask[0] = masks[0]

        stack = [(0, 0, 0)]
        timer = 0

        while stack:
            u, p, idx = stack.pop()
            if idx == 0:
                timer += 1
                tin[u] = timer
                up[u][0] = p
                for i in range(1, LOGN):
                    up[u][i] = up[up[u][i-1]][i-1]
            
            if idx < len(adj[u]):
                v = adj[u][idx]
                stack.append((u, p, idx + 1))
                if v != p:
                    depth[v] = depth[u] + 1
                    path_mask[v] = path_mask[u] ^ masks[v]
                    stack.append((v, u, 0))
            else:
                tout[u] = timer

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOGN):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOGN - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        bit = [0] * (timer + 2)

        def bit_update(idx, val):
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        A = [0] * (timer + 1)
        for i in range(n):
            A[tin[i]] = path_mask[i]

        D = [0] * (timer + 2)
        for i in range(1, timer + 1):
            D[i] = A[i] ^ A[i-1]

        for i in range(1, timer + 1):
            bit[i] ^= D[i]
            nxt = i + (i & (-i))
            if nxt < len(bit):
                bit[nxt] ^= bit[i]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                diff = masks[u] ^ new_mask
                masks[u] = new_mask
                bit_update(tin[u], diff)
                bit_update(tout[u] + 1, diff)
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                res_mask = bit_query(tin[u]) ^ bit_query(tin[v]) ^ masks[lca]
                ans.append(res_mask.bit_count() <= 1)

        return ans
