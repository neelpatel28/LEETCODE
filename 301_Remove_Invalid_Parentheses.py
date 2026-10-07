class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        def calculate_rem(string):
            l = r = 0
            for c in string:
                if c == '(': 
                    l += 1
                elif c == ')':
                    if l > 0: 
                        l -= 1
                    else: 
                        r += 1
            return l, r

        def isValid(string):
            cnt = 0
            for c in string:
                if c == '(': 
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0: 
                        return False
            return cnt == 0

        def recurse(curr_str, start, l, r):
            if l == 0 and r == 0:
                if isValid(curr_str):
                    ans.append(curr_str)
                return
            
            for i in range(start, len(curr_str)):
                if i > start and curr_str[i] == curr_str[i - 1]:
                    continue
                
                if l > 0 and curr_str[i] == '(':
                    recurse(curr_str[:i] + curr_str[i+1:], i, l - 1, r)
                if r > 0 and curr_str[i] == ')':
                    recurse(curr_str[:i] + curr_str[i+1:], i, l, r - 1)

        l_to_rem, r_to_rem = calculate_rem(s)
        recurse(s, 0, l_to_rem, r_to_rem)
        return ans
