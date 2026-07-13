class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for start in range(1, 10):
            value = start
            while value <= high:
                if value >= low:
                    result.append(value)
                last_digit = value % 10
                if last_digit == 9:
                    break
                value = value * 10 + last_digit + 1
        return sorted(result)
