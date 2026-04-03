class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)

        # Step 1: Validate diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # Step 2: Build string
        res = [''] * n
        cur_char = 0  # 0 -> 'a'

        for i in range(n):
            if res[i] == '':
                if cur_char >= 26:
                    return ""
                ch = chr(ord('a') + cur_char)
                cur_char += 1

                # assign same char for all j where lcp[i][j] > 0
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = ch

        word = "".join(res)

        # Step 3: Verify LCP matrix
        # Build LCP from word
        dp = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        dp[i][j] = dp[i+1][j+1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

                # Validate on the fly
                if dp[i][j] != lcp[i][j]:
                    return ""

        return word