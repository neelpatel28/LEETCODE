class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """

        def is_valid(q, d):
            diff = 0
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        res = []

        for q in queries:
            for d in dictionary:
                if is_valid(q, d):
                    res.append(q)
                    break  # no need to check further

        return res