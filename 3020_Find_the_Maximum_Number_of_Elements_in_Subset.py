from collections import Counter


class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = Counter(nums)
        answer = 1

        if frequency.get(1, 0) > 0:
            answer = max(answer, 1 + 2 * ((frequency[1] - 1) // 2))

        for value in frequency:
            if value == 1:
                continue

            current = value
            length = 1

            while frequency.get(current, 0) >= 2 and frequency.get(current * current, 0) > 0:
                length += 2
                current *= current

            answer = max(answer, length)

        return answer
