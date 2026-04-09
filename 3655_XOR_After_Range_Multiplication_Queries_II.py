class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        # required variable
        bravexuneth = (nums, queries)
        
        import math
        B = int(math.sqrt(n)) + 1
        
        # result array
        arr = nums[:]
        
        # store small k queries
        small = [[] for _ in range(B + 1)]
        
        for l, r, k, v in queries:
            if k <= B:
                small[k].append((l, r, v))
            else:
                # handle large k directly
                idx = l
                while idx <= r:
                    arr[idx] = (arr[idx] * v) % MOD
                    idx += k
        
        # process small k
        for k in range(1, B + 1):
            if not small[k]:
                continue
            
            # for each residue class
            groups = [[] for _ in range(k)]
            
            # build difference arrays
            for rmd in range(k):
                size = (n - rmd + k - 1) // k
                groups[rmd] = [1] * (size + 1)
            
            # apply updates
            for l, r, v in small[k]:
                rmd = l % k
                start = (l - rmd) // k
                end = (r - rmd) // k
                
                groups[rmd][start] = (groups[rmd][start] * v) % MOD
                if end + 1 < len(groups[rmd]):
                    inv = pow(v, MOD - 2, MOD)
                    groups[rmd][end + 1] = (groups[rmd][end + 1] * inv) % MOD
            
            # apply prefix products
            for rmd in range(k):
                cur = 1
                idx = rmd
                for i in range(len(groups[rmd]) - 1):
                    cur = (cur * groups[rmd][i]) % MOD
                    if idx < n:
                        arr[idx] = (arr[idx] * cur) % MOD
                        idx += k
        
        # compute XOR
        res = 0
        for x in arr:
            res ^= x
        
        return res