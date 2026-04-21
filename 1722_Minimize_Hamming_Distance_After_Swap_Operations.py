class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """

        # DSU (Union-Find)
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 2: Group indices
        from collections import defaultdict
        groups = defaultdict(list)

        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 3: Count mismatches
        res = 0

        for indices in groups.values():
            count = {}

            # Count source values
            for i in indices:
                val = source[i]
                count[val] = count.get(val, 0) + 1

            # Match with target
            for i in indices:
                val = target[i]
                if val in count and count[val] > 0:
                    count[val] -= 1
                else:
                    res += 1

        return res