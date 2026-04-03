class Solution(object):
    def getHappyString(self, n, k):
        res = []
        
        def backtrack(curr):
            if len(res) >= k:
                return
            
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        
        backtrack("")
        
        if k <= len(res):
            return res[k-1]
        return ""   