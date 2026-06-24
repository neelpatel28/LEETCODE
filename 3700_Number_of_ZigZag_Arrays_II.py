class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        
        def mult(A, B):
            size = len(A)
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k]:
                        for j in range(size):
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        
        def power(A, p):
            size = len(A)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while p:
                if p & 1:
                    result = mult(result, A)
                A = mult(A, A)
                p >>= 1
            return result
        
        size = m * 2
        trans = [[0] * size for _ in range(size)]
        
        for v in range(m):
            for v_next in range(v):
                trans[v_next * 2 + 1][v * 2 + 0] = 1
            for v_next in range(v + 1, m):
                trans[v_next * 2 + 0][v * 2 + 1] = 1
        
        state = [0] * size
        for v in range(m):
            state[v * 2 + 0] = v
            state[v * 2 + 1] = m - 1 - v
        
        trans_pow = power(trans, n - 2)
        
        result = [0] * size
        for i in range(size):
            for j in range(size):
                result[i] = (result[i] + trans_pow[i][j] * state[j]) % MOD
        
        return sum(result) % MOD
