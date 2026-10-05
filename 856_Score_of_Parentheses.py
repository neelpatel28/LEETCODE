class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                current_score = stack.pop()
                stack[-1] += max(2 * current_score, 1)
                
        return stack.pop()
