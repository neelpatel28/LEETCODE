class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Frequency arrays for even and odd indices
        even1 = [0] * 26
        odd1 = [0] * 26
        even2 = [0] * 26
        odd2 = [0] * 26

        n = len(s1)

        for i in range(n):
            if i % 2 == 0:
                even1[ord(s1[i]) - ord('a')] += 1
                even2[ord(s2[i]) - ord('a')] += 1
            else:
                odd1[ord(s1[i]) - ord('a')] += 1
                odd2[ord(s2[i]) - ord('a')] += 1

        return even1 == even2 and odd1 == odd2s