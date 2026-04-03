class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1

        mask = 1
        while mask <= n:
            mask = (mask << 1)

        mask = mask - 1
        return mask ^ n
    
    
obj = Solution()   
ans = obj.bitwiseComplement(5) # Output: 2
print(ans)  

ans = obj.bitwiseComplement(58) # Output: 5
print(ans)

ans = obj.bitwiseComplement(546) # Output: 477
print(ans)

ans = obj.bitwiseComplement(8975) # Output: 7408
print(ans)
