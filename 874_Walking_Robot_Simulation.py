class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # Convert obstacles to set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  # start facing North
        
        x, y = 0, 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:  # turn right
                d = (d + 1) % 4
            elif cmd == -2:  # turn left
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    
                    # Check obstacle
                    if (nx, ny) in obstacle_set:
                        break
                    
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist