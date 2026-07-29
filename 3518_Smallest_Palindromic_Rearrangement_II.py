class Solution(object):
    def smallestPalindrome(self, s, k):
        from collections import Counter

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def comb_limited(n, r, limit):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            num = 1
            den = 1
            for i in range(1, r + 1):
                num *= (n - r + i)
                den *= i
                g = gcd(num, den)
                num //= g
                den //= g
                if num > limit:
                    return limit + 1
            return num // den

        def count_perms(cnt, limit):
            total = sum(cnt.values())
            res = 1
            for c in cnt:
                x = cnt[c]
                if x > 0:
                    ways = comb_limited(total, x, limit)
                    res *= ways
                    if res > limit:
                        return limit + 1
                    total -= x
            return res

        freq = Counter(s)
        half = {}
        mid = ""
        for c in sorted(freq):
            if freq[c] % 2:
                mid = c
            half[c] = freq[c] // 2

        total = count_perms(half, k)
        if total < k:
            return ""

        res = []
        chars = sorted(half.keys())

        for _ in range(sum(half.values())):
            for c in chars:
                if half[c] == 0:
                    continue
                half[c] -= 1
                cnt = count_perms(half, k)
                if cnt >= k:
                    res.append(c)
                    break
                else:
                    k -= cnt
                    half[c] += 1

        first_half = "".join(res)
        return first_half + mid + first_half[::-1]