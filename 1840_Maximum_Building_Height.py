class Solution:
    def maxBuilding(self, n, restrictions):
        if not restrictions:
            return n - 1
        
        points = [[1, 0]] + restrictions
        points.sort()
        
        for i in range(1, len(points)):
            max_from_left = points[i - 1][1] + (points[i][0] - points[i - 1][0])
            points[i][1] = min(points[i][1], max_from_left)
        
        for i in range(len(points) - 2, -1, -1):
            max_from_right = points[i + 1][1] + (points[i + 1][0] - points[i][0])
            points[i][1] = min(points[i][1], max_from_right)
        
        max_height = 0
        for i in range(len(points) - 1):
            distance = points[i + 1][0] - points[i][0]
            peak = (points[i][1] + points[i + 1][1] + distance) // 2
            max_height = max(max_height, peak)
        
        last_pos, last_height = points[-1]
        if last_pos < n:
            max_height = max(max_height, last_height + (n - last_pos))
        
        return max_height