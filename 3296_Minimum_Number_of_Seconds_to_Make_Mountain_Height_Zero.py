class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):

        def max_height(t, T):
            l, r = 0, mountainHeight
            ans = 0
            
            while l <= r:
                m = (l + r) // 2
                if t * m * (m + 1) // 2 <= T:
                    ans = m
                    l = m + 1
                else:
                    r = m - 1
            
            return ans

        def possible(T):
            total = 0
            for t in workerTimes:
                total += max_height(t, T)
                if total >= mountainHeight:
                    return True
            return False

        l = 1
        r = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while l < r:
            m = (l + r) // 2
            if possible(m):
                r = m
            else:
                l = m + 1

        return l