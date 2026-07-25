class Solution:
    def maxProduct(self, n):
        a = b = 0
        while n:
            n, d = divmod(n, 10)
            if d >= a:
                a, b = d, a
            elif d > b:
                b = d
        return a * b
