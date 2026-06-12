class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mod = 10**9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Root the tree at node 1 and compute parent/depth.
        LOG = (n + 1).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        stack = [(1, 0, 0)]
        while stack:
            node, d, par = stack.pop()
            depth[node] = d
            parent[0][node] = par
            for nei in graph[node]:
                if nei == par:
                    continue
                stack.append((nei, d + 1, node))

        for i in range(1, LOG):
            for node in range(1, n + 1):
                parent[i][node] = parent[i - 1][parent[i - 1][node]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if parent[i][u] != parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]
            return parent[0][u]

        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]
            answer.append(pow(2, dist - 1, mod))
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]]))  # [0, 1]
    print(sol.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]))  # [2, 1, 4]
