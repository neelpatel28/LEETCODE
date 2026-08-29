class Solution(object):

    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        sorted_pairs = sorted((num, i) for i, num in enumerate(nums))

        groups = []
        for pair in sorted_pairs:
            if not groups or pair[0] - groups[-1][-1][0] > limit:
                groups.append([pair])
            else:
                groups[-1].append(pair)

        res = [0] * n

        for group in groups:
            values = sorted(pair[0] for pair in group)
            indices = sorted(pair[1] for pair in group)

            for val, idx in zip(values, indices):
                res[idx] = val

        return res
