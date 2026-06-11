MOD = 10**9 + 7


class Solution(object):
    def numberOfWays(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges) + 1
        if n == 1:
            return 0

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS from root 1 to determine max depth
        from collections import deque

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        depth = 0

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                for nx in graph[node]:
                    if not visited[nx]:
                        visited[nx] = True
                        q.append(nx)

        # The depth of the root is 0, so max number of edges is depth-1.
        # But since we increment depth for each BFS level starting from the root,
        # the number of edges in the deepest path is exactly depth - 1.
        max_edges = depth - 1
        return pow(2, max_edges - 1, MOD)


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfWays([[1, 2]]))  # expect 1
    print(s.numberOfWays([[1, 2], [1, 3], [3, 4], [3, 5]]))  # expect 2
