class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for ch in s:
            if ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                # duplicate current result (use slice copy for compatibility)
                res.extend(res[:])
            elif ch == '%':
                # reverse current result
                res.reverse()
            else:
                # lowercase letter: append
                res.append(ch)
        return ''.join(res)