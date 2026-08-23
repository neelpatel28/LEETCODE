class Solution:

    def sumGame(self, num):
        n = len(num)
        mid = n // 2

        # Extract values for the left half
        left_sum = sum(int(c) for c in num[:mid] if c != "?")
        left_q = num[:mid].count("?")

        # Extract values for the right half
        right_sum = sum(int(c) for c in num[mid:] if c != "?")
        right_q = num[mid:].count("?")

        # Compute differences
        sum_diff = left_sum - right_sum
        q_diff = left_q - right_q

        # If the total number of '?' is odd, Alice wins automatically
        if (left_q + right_q) % 2 != 0:
            return True

        # Bob wins if pairs of 9 can perfectly balance the sum difference
        return sum_diff + (q_diff // 2) * 9 != 0
