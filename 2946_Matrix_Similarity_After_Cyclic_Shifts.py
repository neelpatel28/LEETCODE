class Solution(object):
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        shift = k % n
        
        if shift == 0:
            return True
        
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row → left shift
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                else:
                    # odd row → right shift
                    if mat[i][j] != mat[i][(j - shift) % n]:
                        return False
        
        return True