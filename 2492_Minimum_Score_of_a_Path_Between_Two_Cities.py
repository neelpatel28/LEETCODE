class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adjacency = [[] for _ in range(n + 1)]
        for city1, city2, distance in roads:
            adjacency[city1].append((city2, distance))
            adjacency[city2].append((city1, distance))

        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        minimum_score = float("inf")

        while stack:
            city = stack.pop()
            for neighbor, distance in adjacency[city]:
                minimum_score = min(minimum_score, distance)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return minimum_score
