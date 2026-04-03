class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1

        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero+1):
            for j in range(1, one+1):
                
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i - limit - 1 >= 0:
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j]) % MOD
                
                dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j - limit - 1 >= 0:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD