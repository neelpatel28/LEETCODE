class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            parts = []

            for i in range(0, len(s), k):
                total = sum(int(ch) for ch in s[i:i + k])
                parts.append(str(total))

            s = ''.join(parts)

        return s
