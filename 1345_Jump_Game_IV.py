class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0

        graph = {}
        for i in range(n):
            v = arr[i]
            if v in graph:
                graph[v].append(i)
            else:
                graph[v] = [i]

        visited = [False] * n
        visited[0] = True

        queue = [0]
        front = 0
        steps = 0

        while front < len(queue):
            level_size = len(queue) - front

            for _ in range(level_size):
                i = queue[front]
                front += 1

                if i == n - 1:
                    return steps

                ni = i + 1
                if ni < n and not visited[ni]:
                    visited[ni] = True
                    queue.append(ni)

                ni = i - 1
                if ni >= 0 and not visited[ni]:
                    visited[ni] = True
                    queue.append(ni)

                v = arr[i]
                if v in graph:
                    for nei in graph[v]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)
                    del graph[v]

            steps += 1

        return -1