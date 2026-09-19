class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        squared_distance = (distance_x * distance_x) + (distance_y * distance_y)
        
        return squared_distance <= (radius * radius)
