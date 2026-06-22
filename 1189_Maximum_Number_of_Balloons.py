class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import Counter
        
        char_count = Counter(text)
        
        b_count = char_count['b'] // 1
        a_count = char_count['a'] // 1
        l_count = char_count['l'] // 2
        o_count = char_count['o'] // 2
        n_count = char_count['n'] // 1
        
        return min(b_count, a_count, l_count, o_count, n_count)

