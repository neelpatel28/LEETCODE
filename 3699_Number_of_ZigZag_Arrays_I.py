class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        range_size = r - l + 1
        
        count_up = [v for v in range(range_size)]
        count_down = [range_size - 1 - v for v in range(range_size)]
        
        for pos in range(3, n + 1):
            new_count_up = [0] * range_size
            new_count_down = [0] * range_size
            
            suffix_up = [0] * (range_size + 1)
            for i in range(range_size - 1, -1, -1):
                suffix_up[i] = (suffix_up[i + 1] + count_up[i]) % MOD
            
            prefix_down = [0] * (range_size + 1)
            for i in range(range_size):
                prefix_down[i + 1] = (prefix_down[i] + count_down[i]) % MOD
            
            for v in range(range_size):
                new_count_down[v] = suffix_up[v + 1]
                new_count_up[v] = prefix_down[v]
            
            count_up = new_count_up
            count_down = new_count_down
        
        return (sum(count_up) + sum(count_down)) % MOD
