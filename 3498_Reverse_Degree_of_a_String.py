class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_sum = 0
        for i, char in enumerate(s, start=1):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            total_sum += rev_alphabet_pos * i
        return total_sum
