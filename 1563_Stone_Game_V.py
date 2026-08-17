class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            k = 0
            for i in range(n - length + 1):
                j = i + length - 1
                while k < j and pref[k + 1] - pref[i] < pref[j + 1] - pref[k + 1]:
                    k += 1

                res = 0
                if i <= k - 1:
                    res = max(res, max_l[i][k - 1])
                if k + 1 <= j:
                    res = max(res, max_r[k + 1][j])

                if k < j and pref[k + 1] - pref[i] == pref[j + 1] - pref[k + 1]:
                    res = max(res, max_l[i][k])

                dp[i][j] = res
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + pref[j + 1] - pref[i])
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + pref[j + 1] - pref[i])

        return dp[0][n - 1]
