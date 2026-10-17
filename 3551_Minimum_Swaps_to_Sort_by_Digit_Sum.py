class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each number with its original index: (value, original_index)
        arr = [(val, i) for i, val in enumerate(nums)]
        
        # Sort based on custom rules: 1st by digit sum, 2nd by numerical value
        arr.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        swaps = 0
        
        # Trace cycles to find the minimum number of swaps
        for i in range(n):
            # Skip if already visited or already in the correct sorted position
            if visited[i] or arr[i][1] == i:
                continue
                
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][1]  # Move to the original index of the element currently here
                cycle_size += 1
                
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps
