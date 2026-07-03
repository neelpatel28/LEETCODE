class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        if n <= 1:
            return -1

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1

        queue = []
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        topology = []
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            topology.append(node)
            for neighbor, _ in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topology) != n:
            return -1

        costs = sorted({cost for _, _, cost in edges})

        def feasible(threshold):
            dist = [float('inf')] * n
            dist[0] = 0
            for node in topology:
                if dist[node] == float('inf'):
                    continue
                if node == n - 1:
                    return True
                for neighbor, cost in graph[node]:
                    if cost < threshold:
                        continue
                    if neighbor != n - 1 and not online[neighbor]:
                        continue
                    next_cost = dist[node] + cost
                    if next_cost <= k and next_cost < dist[neighbor]:
                        dist[neighbor] = next_cost
            return dist[n - 1] <= k

        if not feasible(costs[0] if costs else 0):
            return -1

        left, right = 0, len(costs) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if feasible(costs[mid]):
                answer = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return answer
