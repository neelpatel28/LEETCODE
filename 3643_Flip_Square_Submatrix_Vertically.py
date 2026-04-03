class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        top = x
        bottom = x + k - 1
        
        while top < bottom:
            for col in range(y, y + k):
                # Swap elements
                grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
            
            top += 1
            bottom -= 1
        
        return grid