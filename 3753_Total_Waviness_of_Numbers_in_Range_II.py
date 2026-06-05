class Solution(object):
    def totalWaviness(self, num1, num2):
        
        def solve(n):
            if n <= 0:
                return 0

            s = str(n)
            memo = {}

            def dfs(i, prev2, prev1, tight, started):
                key = (i, prev2, prev1, tight, started)
                if key in memo:
                    return memo[key]

                if i == len(s):
                    return (1, 0)

                limit = int(s[i]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # Leading zeros
                    if not started:
                        if d == 0:
                            cnt, wav = dfs(i + 1, -1, -1, ntight, False)
                        else:
                            cnt, wav = dfs(i + 1, -1, d, ntight, True)

                        total_cnt += cnt
                        total_wav += wav

                    # Number started
                    else:
                        if prev2 == -1:
                            cnt, wav = dfs(i + 1, prev1, d, ntight, True)
                            total_cnt += cnt
                            total_wav += wav
                        else:
                            add = 0
                            if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                add = 1

                            cnt, wav = dfs(i + 1, prev1, d, ntight, True)
                            total_cnt += cnt
                            total_wav += wav + cnt * add

                memo[key] = (total_cnt, total_wav)
                return memo[key]

            return dfs(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)