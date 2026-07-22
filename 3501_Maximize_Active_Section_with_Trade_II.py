import bisect

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)

        # 1. find zero-runs (maximal blocks of '0')
        starts = []
        ends = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                starts.append(i)
                ends.append(j - 1)
                i = j
            else:
                i += 1

        R = len(starts)
        lengths = [ends[k] - starts[k] + 1 for k in range(R)]
        total_ones = n - sum(lengths)

        # 2. adjacent-pair sums for interior (non-clipped) queries
        C = [lengths[k] + lengths[k + 1] for k in range(R - 1)] if R >= 2 else []

        # 3. sparse table over C for O(1) range-max queries
        st = None
        LOG = None
        if C:
            m = len(C)
            LOG = [0] * (m + 1)
            for x in range(2, m + 1):
                LOG[x] = LOG[x // 2] + 1
            K = LOG[m] + 1
            st = [C[:]]
            for k in range(1, K):
                prev = st[-1]
                half = 1 << (k - 1)
                cur_len = m - (1 << k) + 1
                if cur_len <= 0:
                    break
                cur = [0] * cur_len
                for idx in range(cur_len):
                    a = prev[idx]
                    b = prev[idx + half]
                    cur[idx] = a if a > b else b
                st.append(cur)

        def range_max(l, r):
            # inclusive range over C, assumes l<=r and valid indices
            k = LOG[r - l + 1]
            a = st[k][l]
            b = st[k][r - (1 << k) + 1]
            return a if a > b else b

        answer = [0] * len(queries)

        for qi, (l, r) in enumerate(queries):
            if R < 2:
                answer[qi] = total_ones
                continue

            # first zero-run index with end >= l
            i_idx = bisect.bisect_left(ends, l)
            # last zero-run index with start <= r
            j_idx = bisect.bisect_right(starts, r) - 1

            if i_idx > j_idx or i_idx >= R or j_idx < 0:
                answer[qi] = total_ones
                continue

            m_cnt = j_idx - i_idx + 1
            if m_cnt < 2:
                answer[qi] = total_ones
                continue

            clipped_first = ends[i_idx] - max(starts[i_idx], l) + 1
            clipped_last = min(ends[j_idx], r) - starts[j_idx] + 1

            if m_cnt == 2:
                gain = clipped_first + clipped_last
            else:
                term1 = clipped_first + lengths[i_idx + 1]
                term2 = lengths[j_idx - 1] + clipped_last
                best = term1 if term1 > term2 else term2
                if m_cnt >= 4:
                    rmax = range_max(i_idx + 1, j_idx - 2)
                    if rmax > best:
                        best = rmax
                gain = best

            answer[qi] = total_ones + gain

        return answer