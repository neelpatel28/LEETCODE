class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """

        # reverse using math
        x = n
        rev = 0

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        return abs(n - rev)