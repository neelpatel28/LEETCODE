import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Release servers that have completed their requests
            while busy and busy[0][0] <= start:
                finish, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find the first available server >= i % k
            target = i % k
            pos = available.bisect_left(target)

            if pos == len(available):
                pos = 0

            server = available.pop(pos)

            count[server] += 1
            heapq.heappush(busy, (start + duration, server))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]
