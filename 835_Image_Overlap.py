class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        ones1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        ones2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        from collections import Counter
        counts = Counter((r1 - r2, c1 - c2) for r1, c1 in ones1 for r2, c2 in ones2)
        
        return max(counts.values()) if counts else 0
