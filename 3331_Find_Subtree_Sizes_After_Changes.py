class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Track the most recent ancestor for each character
        last_seen = [-1] * 26

        # Store the previous occurrence of each node's character
        prev = [-1] * n

        # Every node initially contributes 1 to its subtree
        ans = [1] * n

        # Iterative DFS: (node, state)
        # state 0 = entering, state 1 = exiting
        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()
            char_idx = ord(s[node]) - ord('a')

            if state == 0:
                # Save the nearest matching ancestor
                prev[node] = last_seen[char_idx]

                # Current node becomes the nearest matching ancestor
                last_seen[char_idx] = node

                # Process node after all its children
                stack.append((node, 1))

                # Traverse original children
                for child in reversed(children[node]):
                    stack.append((child, 0))

            else:
                # Restore the previous ancestor for this character
                last_seen[char_idx] = prev[node]

                # Determine the node's final parent
                new_parent = (
                    prev[node]
                    if prev[node] != -1
                    else parent[node]
                )

                # Aggregate subtree size into its final parent
                if new_parent != -1:
                    ans[new_parent] += ans[node]

        return ans
