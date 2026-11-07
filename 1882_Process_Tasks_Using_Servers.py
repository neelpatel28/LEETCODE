import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []

        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, advance time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the server with minimum weight, then index
            weight, index = heapq.heappop(available)

            result.append(index)

            # Mark the server as busy
            heapq.heappush(
                busy,
                (time + duration, weight, index)
            )

        return result
