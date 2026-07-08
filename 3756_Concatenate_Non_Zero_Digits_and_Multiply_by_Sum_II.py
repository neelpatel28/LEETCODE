from bisect import bisect_left, bisect_right


class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        positions = []
        digits = []
        for index, char in enumerate(s):
            if char != '0':
                positions.append(index)
                digits.append(ord(char) - 48)

        if not digits:
            return [0] * len(queries)

        prefix_value = [0] * (len(digits) + 1)
        prefix_sum = [0] * (len(digits) + 1)
        powers = [1] * (len(s) + 1)
        for index in range(1, len(s) + 1):
            powers[index] = (powers[index - 1] * 10) % MOD

        for index, digit in enumerate(digits, 1):
            prefix_value[index] = (prefix_value[index - 1] * 10 + digit) % MOD
            prefix_sum[index] = prefix_sum[index - 1] + digit

        answer = []
        for left, right in queries:
            start = bisect_left(positions, left)
            end = bisect_right(positions, right) - 1
            if start > end:
                answer.append(0)
                continue

            length = end - start + 1
            value = (prefix_value[end + 1] - prefix_value[start] * powers[length]) % MOD
            total = prefix_sum[end + 1] - prefix_sum[start]
            answer.append((value * total) % MOD)

        return answer
