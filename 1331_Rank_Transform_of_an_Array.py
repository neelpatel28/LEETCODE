class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {value: index + 1 for index, value in enumerate(sorted(set(arr)))}
        return [ranks[value] for value in arr]
