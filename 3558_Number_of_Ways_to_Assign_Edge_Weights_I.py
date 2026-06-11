class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS/DFS from node 1 to compute maximum depth.
        max_depth = 0
        stack = [(1, 0, -1)]
        while stack:
            node, depth, parent = stack.pop()
            max_depth = max(max_depth, depth)
            for nei in graph[node]:
                if nei == parent:
                    continue
                stack.append((nei, depth + 1, node))

        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, mod)


if __name__ == "__main__":
    sol = Solution()
    print(sol.assignEdgeWeights([[1, 2]]))  # 1
    print(sol.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))  # 2
