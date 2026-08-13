class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        s_list = list(s)

        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_pchar = [''] * (4 * n)
        tree_schar = [''] * (4 * n)
        tree_size = [0] * (4 * n)

        def merge(node, left, right):
            tree_size[node] = tree_size[left] + tree_size[right]
            tree_pchar[node] = tree_pchar[left]
            tree_schar[node] = tree_schar[right]

            tree_pref[node] = tree_pref[left]
            tree_suff[node] = tree_suff[right]
            tree_max[node] = max(tree_max[left], tree_max[right])

            if tree_schar[left] == tree_pchar[right]:
                bridge = tree_suff[left] + tree_pref[right]
                if bridge > tree_max[node]:
                    tree_max[node] = bridge

                if tree_pref[left] == tree_size[left]:
                    tree_pref[node] = tree_size[left] + tree_pref[right]
                if tree_suff[right] == tree_size[right]:
                    tree_suff[node] = tree_size[right] + tree_suff[left]

        def build(node, start, end):
            if start == end:
                tree_max[node] = 1
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_pchar[node] = s_list[start]
                tree_schar[node] = s_list[start]
                tree_size[node] = 1
                return

            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            build(left, start, mid)
            build(right, mid + 1, end)
            merge(node, left, right)

        def update(node, start, end, idx, char):
            if start == end:
                tree_pchar[node] = char
                tree_schar[node] = char
                return

            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2

            if idx <= mid:
                update(left, start, mid, idx, char)
            else:
                update(right, mid + 1, end, idx, char)

            merge(node, left, right)

        build(0, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]

            if s_list[idx] != char:
                s_list[idx] = char
                update(0, 0, n - 1, idx, char)

            ans.append(tree_max[0])

        return ans
