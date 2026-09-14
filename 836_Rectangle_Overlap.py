class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # rec1 = [x1, y1, x2, y2]
        # rec2 = [x1, y1, x2, y2]
        
        # Check if rec2 is completely to the left, right, below, or above rec1
        if (rec2[2] <= rec1[0] or  # rec2 is completely to the left of rec1
            rec2[0] >= rec1[2] or  # rec2 is completely to the right of rec1
            rec2[3] <= rec1[1] or  # rec2 is completely below rec1
            rec2[1] >= rec1[3]):   # rec2 is completely above rec1
            return False
            
        return True
