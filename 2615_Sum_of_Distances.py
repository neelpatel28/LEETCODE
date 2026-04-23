class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        from collections import defaultdict

        groups = defaultdict(list)
        
        for i, num in enumerate(nums):
            groups[num].append(i)

        res = [0] * len(nums)

        for indices in groups.values():
            n = len(indices)
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            for k in range(n):
                i = indices[k]
                left = k * i - prefix[k]
                right = (prefix[n] - prefix[k + 1]) - (n - k - 1) * i
                res[i] = left + right

        return res