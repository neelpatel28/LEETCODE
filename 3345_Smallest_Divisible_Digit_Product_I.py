class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            x = n
            p = 1
            if x == 0:
                p = 0
            else:
                while x > 0:
                    p *= x % 10
                    x //= 10
            if p % t == 0:
                return n
            n += 1
