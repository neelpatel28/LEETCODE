class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        # Coordinate compression + unique sentinel
        vals = sorted(set(nums))
        mp = {v: i + 1 for i, v in enumerate(vals)}
        s = [mp[x] for x in nums] + [0]

        m = n + 1

        # Build suffix array using cyclic shifts
        sa = sorted(range(m), key=lambda i: s[i])

        rank = [0] * m
        classes = 1
        rank[sa[0]] = 0

        for i in range(1, m):
            if s[sa[i]] != s[sa[i - 1]]:
                classes += 1
            rank[sa[i]] = classes - 1

        length = 1

        while length < m:
            shifted = [(i - length) % m for i in sa]

            count = [0] * classes

            for i in shifted:
                count[rank[i]] += 1

            for i in range(1, classes):
                count[i] += count[i - 1]

            new_sa = [0] * m

            for i in range(m - 1, -1, -1):
                x = shifted[i]
                c = rank[x]
                count[c] -= 1
                new_sa[count[c]] = x

            sa = new_sa

            new_rank = [0] * m
            new_classes = 1
            new_rank[sa[0]] = 0

            for i in range(1, m):
                cur = sa[i]
                prev = sa[i - 1]

                if (
                    rank[cur] != rank[prev]
                    or rank[(cur + length) % m]
                    != rank[(prev + length) % m]
                ):
                    new_classes += 1

                new_rank[cur] = new_classes - 1

            rank = new_rank
            classes = new_classes
            length *= 2

        # Remove sentinel suffix
        sa = [i for i in sa if i != n]

        # Build inverse suffix array
        pos = [0] * n

        for r, start in enumerate(sa):
            pos[start] = r

        # Kasai's LCP algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                h = 0
                continue

            j = sa[r - 1]

            while (
                i + h < n
                and j + h < n
                and nums[i + h] == nums[j + h]
            ):
                h += 1

            lcp[r] = h

            if h:
                h -= 1

        # Find the shortest unique subarray
        ans = n

        for r in range(n):
            start = sa[r]

            longest = lcp[r]

            if r + 1 < n:
                longest = max(longest, lcp[r + 1])

            candidate = longest + 1

            # Candidate must fit inside the original suffix
            if candidate <= n - start:
                ans = min(ans, candidate)

        return ans
