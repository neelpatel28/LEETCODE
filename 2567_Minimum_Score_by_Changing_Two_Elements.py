class Solution(object):
    def minimizeSum(self, nums):
        INF = float('inf')

        # Three smallest elements
        a = b = c = INF

        # Three largest elements
        x = y = z = -INF

        for num in nums:
            # Maintain three smallest
            if num <= a:
                c, b, a = b, a, num
            elif num <= b:
                c, b = b, num
            elif num < c:
                c = num

            # Maintain three largest
            if num >= z:
                x, y, z = y, z, num
            elif num >= y:
                x, y = y, num
            elif num > x:
                x = num

        return min(z - c, y - b, x - a)
