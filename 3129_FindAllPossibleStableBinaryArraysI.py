class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for i in range(1, min(limit, zero)+1):
            dp0[i][0] = 1
        
        for j in range(1, min(limit, one)+1):
            dp1[0][j] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                
                if i > 0:
                    for k in range(1, min(limit, i)+1):
                        dp0[i][j] = (dp0[i][j] + dp1[i-k][j]) % MOD
                
                if j > 0:
                    for k in range(1, min(limit, j)+1):
                        dp1[i][j] = (dp1[i][j] + dp0[i][j-k]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD

obj = Solution()        
answer = obj.numberOfStableArrays( zero=1, one=1, limit=1)  
print(answer) # Answer should be 2, as the stable arrays are [0,1] and [1,0]

answer = obj.numberOfStableArrays( zero=2, one=1, limit=1)  
print(answer) # Answer should be 1