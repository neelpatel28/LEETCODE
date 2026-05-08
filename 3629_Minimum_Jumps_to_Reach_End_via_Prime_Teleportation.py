from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, nums):
        n = len(nums)
        
        max_val = max(nums)
        spf = list(range(max_val + 1))
        
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def get_prime_factors(x):
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x //= spf[x]
            return factors
        
        prime_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            for p in get_prime_factors(num):
                prime_to_indices[p].append(i)
        
        queue = deque([(0, 0)]) 
        visited = [False] * n
        visited[0] = True
        
        used_primes = set()
        
        while queue:
            i, steps = queue.popleft()
            
            if i == n - 1:
                return steps
            
            for ni in [i - 1, i + 1]:
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    queue.append((ni, steps + 1))
            
            num = nums[i]
            
            if num > 1 and spf[num] == num:
                p = num
                if p not in used_primes:
                    for ni in prime_to_indices[p]:
                        if not visited[ni]:
                            visited[ni] = True
                            queue.append((ni, steps + 1))
                    used_primes.add(p)
        
        return -1