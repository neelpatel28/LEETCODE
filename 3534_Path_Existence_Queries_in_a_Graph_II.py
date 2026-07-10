class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        order = sorted(range(n), key=lambda i: nums[i])
        position = [0] * n
        for i in range(n):
            position[order[i]] = i

        farthest = [0] * n
        right = 0
        for left in range(n):
            while right < n and nums[order[right]] - nums[order[left]] <= maxDiff:
                right += 1
            farthest[left] = right - 1

        max_power = 17
        jump = [farthest[:]]
        for _ in range(1, max_power):
            prev = jump[-1]
            curr = [0] * n
            for i in range(n):
                curr[i] = prev[prev[i]]
            jump.append(curr)

        answers = []
        for u, v in queries:
            if u == v:
                answers.append(0)
                continue

            left = position[u]
            right = position[v]
            if left > right:
                left, right = right, left

            current = left
            steps = 0

            for power in range(max_power - 1, -1, -1):
                if jump[power][current] < right:
                    current = jump[power][current]
                    steps += 1 << power

            if farthest[current] < right:
                answers.append(-1)
            else:
                answers.append(steps + 1)

        return answers