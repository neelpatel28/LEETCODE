class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Returns the k-th (0-indexed) character of the result after processing `s`.
        If k is out of bounds return '.'.
        """
        n = len(s)
        # lengths after processing prefix up to i (inclusive)
        cap = 10**18
        lens = [0] * n
        L = 0
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                L = L + 1
            elif ch == '*':
                if L > 0:
                    L = L - 1
            elif ch == '#':
                L = L * 2
            elif ch == '%':
                # reverse doesn't change length
                L = L
            if L > cap:
                L = cap
            lens[i] = L

        if n == 0:
            return '.'

        total = lens[-1]
        if k < 0 or k >= total:
            return '.'

        # reverse simulate to map k back
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev = lens[i - 1] if i > 0 else 0
            if 'a' <= ch <= 'z':
                # appended at position prev
                if k == prev:
                    return ch
                # otherwise it must be in the prefix
                # set length back to prev and continue
                # (k remains unchanged)
                # L = prev
            elif ch == '*':
                # removed last char if prev>0; in any case we map to prev
                # k stays same
                pass
            elif ch == '#':
                # duplication: after = prev * 2
                if prev == 0:
                    # nothing changed
                    pass
                else:
                    if k >= prev:
                        k = k - prev
            elif ch == '%':
                if prev == 0:
                    pass
                else:
                    k = prev - 1 - k

        return '.'


if __name__ == '__main__':
    sol = Solution()
    examples = [
        ("a#b%*", 1, 'a'),
        ("cd%#*#", 3, 'd'),
        ("z*#", 0, '.'),
    ]
    for s, k, exp in examples:
        out = sol.processStr(s, k)
        print(s, k, out, 'OK' if out == exp else 'FAIL (expected %s)' % exp)
