from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        seats = defaultdict(int)
        for row, col in reservedSeats:
            if col in (2, 3, 4, 5):
                seats[row] |= 1
            if col in (4, 5, 6, 7):
                seats[row] |= 2
            if col in (6, 7, 8, 9):
                seats[row] |= 4
        
        ans = 2 * (n - len(seats))
        for mask in seats.values():
            left = (mask & 1) == 0
            mid = (mask & 2) == 0
            right = (mask & 4) == 0
            
            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
                
        return ans
