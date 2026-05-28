class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        child = [[-1]*26]
        idx = [-1]
        length = [10**9]

        wc = wordsContainer
        lens = [len(w) for w in wc]

        def new_node():
            child.append([-1]*26)
            idx.append(-1)
            length.append(10**9)
            return len(child) - 1

        for i in range(len(wc)):
            node = 0
            l = lens[i]
            if l < length[0] or (l == length[0] and i < idx[0]):
                length[0] = l
                idx[0] = i

            w = wc[i]
            for j in range(len(w)-1, -1, -1):
                c = ord(w[j]) - 97
                nxt = child[node][c]
                if nxt == -1:
                    nxt = new_node()
                    child[node][c] = nxt
                node = nxt

                if l < length[node] or (l == length[node] and i < idx[node]):
                    length[node] = l
                    idx[node] = i

        res = []
        child_local = child
        idx_local = idx

        for w in wordsQuery:
            node = 0
            ans = idx_local[0]
            for j in range(len(w)-1, -1, -1):
                c = ord(w[j]) - 97
                nxt = child_local[node][c]
                if nxt == -1:
                    break
                node = nxt
                ans = idx_local[node]
            res.append(ans)

        return res