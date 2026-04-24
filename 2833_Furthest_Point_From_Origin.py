class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """

        L = moves.count('L')
        R = moves.count('R')
        blank = moves.count('_')

        return abs(R - L) + blank