class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.sort()
        points = [[1, 0]] + restrictions
        
        for i in range(1, len(points)):
            dist = points[i][0] - points[i-1][0]
            max_from_left = points[i-1][1] + dist
            points[i][1] = min(points[i][1], max_from_left)
        
        for i in range(len(points) - 2, -1, -1):
            dist = points[i+1][0] - points[i][0]
            max_from_right = points[i+1][1] + dist
            points[i][1] = min(points[i][1], max_from_right)
        
        max_height = 0
        for i in range(len(points) - 1):
            dist = points[i+1][0] - points[i][0]
            peak = (points[i][1] + points[i+1][1] + dist) // 2
            max_height = max(max_height, peak)
        
        if points[-1][0] < n:
            max_height = max(max_height, points[-1][1] + (n - points[-1][0]))
        
        return max_height