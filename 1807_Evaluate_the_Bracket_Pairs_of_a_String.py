class Solution(object):
    def evaluate(self, s, knowledge):
        mapping = {key: value for key, value in knowledge}
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                key = s[i+1:j]
                res.append(mapping.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
                
        return "".join(res)
