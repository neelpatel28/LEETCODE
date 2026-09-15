class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        count = 0
        i = 0
        
        while i < n:
            if i + k <= n:
                l1, r1 = i, i + k - 1
                while l1 <= r1 and s[l1] == s[r1]:
                    l1 += 1
                    r1 -= 1
                if l1 > r1:
                    count += 1
                    i += k
                    continue
                    
            if i + k + 1 <= n:
                l2, r2 = i, i + k
                while l2 <= r2 and s[l2] == s[r2]:
                    l2 += 1
                    r2 -= 1
                if l2 > r2:
                    count += 1
                    i += k + 1
                    continue
                    
            i += 1
            
        return count
