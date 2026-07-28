from collections import Counter


class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        left = []
        middle = ""

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if count[ch] == 0:
                continue
            if count[ch] % 2 == 1:
                middle = ch
            half = count[ch] // 2
            left.extend([ch] * half)

        left_str = "".join(left)
        return left_str + middle + left_str[::-1]


# Example usage
if __name__ == "__main__":
    sol = Solution()
    tests = ["z", "babab", "daccad"]
    for test in tests:
        print(sol.smallestPalindrome(test))
