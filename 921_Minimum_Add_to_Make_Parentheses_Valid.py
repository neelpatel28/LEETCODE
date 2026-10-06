class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        balance = 0
        
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
                
            if balance < 0:
                ans += 1
                balance = 0
                
        return ans + balance
