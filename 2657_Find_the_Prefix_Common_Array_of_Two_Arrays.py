class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seen = [0] * (n + 1)
        result = []
        common = 0
        
        for i in range(n):
            # Process A[i]
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                common += 1
            
            # Process B[i]
            seen[B[i]] += 1
            if seen[B[i]] == 2:
                common += 1
            
            result.append(common)
        
        return result