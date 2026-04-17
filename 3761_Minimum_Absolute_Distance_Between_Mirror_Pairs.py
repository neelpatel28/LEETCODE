class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def reverse_num(x):
            return int(str(x)[::-1])

        last_seen = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            if num in last_seen:
                min_dist = min(min_dist, i - last_seen[num])

            rev = reverse_num(num)
            last_seen[rev] = i

        return min_dist if min_dist != float('inf') else -1