class Solution(object):
    def minOperations(self, grid, x):
        # Flatten the grid
        arr = [num for row in grid for num in row]
        
        # Check feasibility
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1
        
        # Sort to find median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Compute operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops
    