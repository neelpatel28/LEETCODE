class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def traverse(start):
            stack = [start]
            node_count = 0
            degree_sum = 0

            while stack:
                node = stack.pop()
                if visited[node]:
                    continue

                visited[node] = True
                node_count += 1
                degree_sum += len(graph[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

            return node_count, degree_sum // 2

        complete_count = 0

        for node in range(n):
            if not visited[node]:
                node_count, edge_count = traverse(node)
                if edge_count == node_count * (node_count - 1) // 2:
                    complete_count += 1

        return complete_count