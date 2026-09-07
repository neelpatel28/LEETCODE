class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ends_with = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            ends_with[idx] = (sum(ends_with) + 1) % MOD
            
        return sum(ends_with) % MOD
