class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        insertions = 0

        for ch in s:
            if ch == '(':
                left += 2

                if left % 2 == 1:
                    insertions += 1
                    left -= 1
            else:
                left -= 1

                if left < 0:
                    insertions += 1
                    left = 1

        return insertions + left
