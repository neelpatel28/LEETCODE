class Solution(object):
    def remainingMethods(self, n, k, invocations):
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
        
        stack = [k]
        suspicious = set([k])
        
        while stack:
            u = stack.pop()
            for v in g[u]:
                if v not in suspicious:
                    suspicious.add(v)
                    stack.append(v)
        
        for u, v in invocations:
            if v in suspicious and u not in suspicious:
                return list(range(n))
        
        return [i for i in range(n) if i not in suspicious]
