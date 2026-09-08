class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        factor = 1000
        
        while n >= factor:
            next_factor = factor * 1000
            count = min(n, next_factor - 1) - factor + 1
            total_commas += count
            factor = next_factor
            
        return total_commas
