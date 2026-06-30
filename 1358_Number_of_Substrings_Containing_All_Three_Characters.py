class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0, 0, 0]
        left = 0
        total = 0

        for right, char in enumerate(s):
            counts[ord(char) - 97] += 1
            while counts[0] > 0 and counts[1] > 0 and counts[2] > 0:
                total += len(s) - right
                counts[ord(s[left]) - 97] -= 1
                left += 1

        return total
