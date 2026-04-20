class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        n = len(colors)
        res = 0

        # Compare with first house
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                res = max(res, j)
                break

        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                res = max(res, n - 1 - i)
                break

        return res