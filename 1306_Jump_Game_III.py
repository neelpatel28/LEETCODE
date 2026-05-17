from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        n = len(arr)
        q = deque([start])
        
        while q:
            i = q.popleft()
            
            if i < 0 or i >= n or arr[i] < 0:
                continue
            
            if arr[i] == 0:
                return True
            
            jump = arr[i]
            arr[i] = -jump
            
            q.append(i + jump)
            q.append(i - jump)
        
        return False