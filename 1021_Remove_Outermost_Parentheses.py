class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If opened > 0, this '(' is not an outermost parenthesis
                if opened > 0:
                    result.append(char)
                opened += 1
            else:
                opened -= 1
                # If opened > 0, this ')' is not an outermost parenthesis
                if opened > 0:
                    result.append(char)
                    
        return "".join(result)
