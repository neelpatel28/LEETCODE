class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        
        energy = 0        # current energy
        initial = 0       # required initial energy
        
        for actual, minimum in tasks:
            # If we don't have enough energy to start this task
            if energy < minimum:
                # Increase initial energy
                diff = minimum - energy
                initial += diff
                energy += diff
            
            # Perform the task
            energy -= actual
        
        return initial