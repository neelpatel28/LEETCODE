class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Precompute proper divisors for every possible length
        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(d * 2, n + 1, d):
                divisors[length].append(d)

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = length

                for d in divisors[length]:
                    groups = length // d
                    changes = 0

                    for offset in range(d):
                        left = i + offset
                        right = i + (groups - 1) * d + offset

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                    if best == 0:
                        break

                cost[i][j] = best

        # dp[i][p] = minimum changes to partition
        # the first i characters into p semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n - 2 * (k - p) + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[i][p] = min(
                        dp[i][p],
                        dp[j][p - 1] + cost[j][i - 1]
                    )

        return dp[n][k]
