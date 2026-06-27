class BinaryIndexedTree:
    __slots__ = ("n", "c")

    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        tree = BinaryIndexedTree(n * 2 + 1)

        s = n + 1
        tree.update(s, 1)

        ans = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1

            ans += tree.query(s - 1)
            tree.update(s, 1)

        return ans