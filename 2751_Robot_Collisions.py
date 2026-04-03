class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        
        # Step 1: Combine all info and sort by position
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
        
        stack = []  # will store indices of robots moving right
        alive = [True] * n
        
        # Convert healths to mutable list
        curr_health = healths[:]
        
        for pos, h, d, idx in robots:
            if d == 'R':
                stack.append(idx)
            else:
                # Moving left → check collisions
                while stack and curr_health[idx] > 0:
                    top = stack[-1]
                    
                    if curr_health[top] < curr_health[idx]:
                        # right robot dies
                        alive[top] = False
                        stack.pop()
                        curr_health[idx] -= 1
                        
                    elif curr_health[top] > curr_health[idx]:
                        # left robot dies
                        alive[idx] = False
                        curr_health[top] -= 1
                        break
                        
                    else:
                        # both die
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
        
        # Collect survivors in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append(curr_health[i])
        
        return result