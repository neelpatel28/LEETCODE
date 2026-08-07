from collections import deque

class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        req = self._factor_t(t)
        if req is None:
            return "-1"

        max2, max3, max5, max7 = req
        dp, dims = self._build_dp(max2, max3, max5, max7)

        n = len(num)
        best_pos = -1
        best_digit = None
        best_rem = None

        prefix2 = prefix3 = prefix5 = prefix7 = 0
        prefix_valid = True
        for i, ch in enumerate(num):
            if not prefix_valid:
                break

            cur = ord(ch) - 48
            lower = cur + 1
            if lower <= 9:
                for d in range(lower, 10):
                    if d == 0:
                        continue
                    used2 = min(max2, prefix2 + _DIGIT_EXP[d][0])
                    used3 = min(max3, prefix3 + _DIGIT_EXP[d][1])
                    used5 = min(max5, prefix5 + _DIGIT_EXP[d][2])
                    used7 = min(max7, prefix7 + _DIGIT_EXP[d][3])
                    rem2 = max2 - used2
                    rem3 = max3 - used3
                    rem5 = max5 - used5
                    rem7 = max7 - used7
                    if self._can_fill(dp, dims, rem2, rem3, rem5, rem7, n - i - 1):
                        best_pos = i
                        best_digit = d
                        best_rem = (rem2, rem3, rem5, rem7)
                        break

            if cur == 0:
                prefix_valid = False
                break

            prefix2 = min(max2, prefix2 + _DIGIT_EXP[cur][0])
            prefix3 = min(max3, prefix3 + _DIGIT_EXP[cur][1])
            prefix5 = min(max5, prefix5 + _DIGIT_EXP[cur][2])
            prefix7 = min(max7, prefix7 + _DIGIT_EXP[cur][3])

        if prefix_valid and prefix2 == max2 and prefix3 == max3 and prefix5 == max5 and prefix7 == max7:
            return num

        if best_pos >= 0:
            suffix = self._build_suffix(n - best_pos - 1, best_rem, dp, dims)
            return num[:best_pos] + str(best_digit) + suffix

        full_need_idx = self._index(max2, max3, max5, max7, dims)
        if dp[full_need_idx] == float("inf"):
            return "-1"

        L = max(n + 1, dp[full_need_idx])
        return self._build_suffix(L, (max2, max3, max5, max7), dp, dims)

    def _factor_t(self, t):
        count2 = count3 = count5 = count7 = 0
        while t % 2 == 0:
            t //= 2
            count2 += 1
        while t % 3 == 0:
            t //= 3
            count3 += 1
        while t % 5 == 0:
            t //= 5
            count5 += 1
        while t % 7 == 0:
            t //= 7
            count7 += 1
        if t != 1:
            return None
        return count2, count3, count5, count7

    def _build_dp(self, max2, max3, max5, max7):
        D2 = max2 + 1
        D3 = max3 + 1
        D5 = max5 + 1
        D7 = max7 + 1
        total = D2 * D3 * D5 * D7
        dp = [float("inf")] * total

        def idx(a, b, c, d):
            return ((a * D3 + b) * D5 + c) * D7 + d

        dp[0] = 0
        q = deque([(0, 0, 0, 0)])
        while q:
            a, b, c, d = q.popleft()
            base = dp[idx(a, b, c, d)]
            for digit in range(2, 10):
                if digit == 0 or digit == 1:
                    continue
                na = min(max2, a + _DIGIT_EXP[digit][0])
                nb = min(max3, b + _DIGIT_EXP[digit][1])
                nc = min(max5, c + _DIGIT_EXP[digit][2])
                nd = min(max7, d + _DIGIT_EXP[digit][3])
                ni = idx(na, nb, nc, nd)
                if dp[ni] > base + 1:
                    dp[ni] = base + 1
                    q.append((na, nb, nc, nd))
        return dp, (D2, D3, D5, D7)

    def _index(self, a, b, c, d, dims):
        D2, D3, D5, D7 = dims
        return ((a * D3 + b) * D5 + c) * D7 + d

    def _can_fill(self, dp, dims, r2, r3, r5, r7, length):
        if length < 0:
            return False
        return dp[self._index(r2, r3, r5, r7, dims)] <= length

    def _build_suffix(self, length, rem, dp, dims):
        rem2, rem3, rem5, rem7 = rem
        result = []
        for pos in range(length):
            remaining = length - pos - 1
            for d in range(1, 10):
                new2 = max(0, rem2 - _DIGIT_EXP[d][0])
                new3 = max(0, rem3 - _DIGIT_EXP[d][1])
                new5 = max(0, rem5 - _DIGIT_EXP[d][2])
                new7 = max(0, rem7 - _DIGIT_EXP[d][3])
                if self._can_fill(dp, dims, new2, new3, new5, new7, remaining):
                    result.append(str(d))
                    rem2, rem3, rem5, rem7 = new2, new3, new5, new7
                    break
        return "".join(result)


_DIGIT_EXP = {
    0: (0, 0, 0, 0),
    1: (0, 0, 0, 0),
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    6: (1, 1, 0, 0),
    7: (0, 0, 0, 1),
    8: (3, 0, 0, 0),
    9: (0, 2, 0, 0),
}
