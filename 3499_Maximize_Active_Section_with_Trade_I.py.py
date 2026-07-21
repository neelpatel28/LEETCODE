class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t = "1" + s + "1"
        runs = []
        prev = t[0]
        cnt = 1
        for c in t[1:]:
            if c == prev:
                cnt += 1
            else:
                runs.append(cnt)
                prev = c
                cnt = 1
        runs.append(cnt)

        Z = []
        for i in range(1, len(runs), 2):
            Z.append(runs[i])

        if len(Z) < 2:
            return s.count('1')

        m = len(Z)
        pref = [0] * m
        suff = [0] * m
        pref[0] = Z[0]
        for i in range(1, m):
            pref[i] = max(pref[i - 1], Z[i])
        suff[m - 1] = Z[m - 1]
        for i in range(m - 2, -1, -1):
            suff[i] = max(suff[i + 1], Z[i])

        base = s.count('1')
        best_gain = 0

        for k in range(1, m):
            one_len = runs[2 * k]
            merged = Z[k - 1] + one_len + Z[k]

            other = 0
            if k - 2 >= 0:
                other = max(other, pref[k - 2])
            if k + 1 < m:
                other = max(other, suff[k + 1])

            best_zero = max(merged, other)
            best_gain = max(best_gain, best_zero - one_len)

        return base + best_gain