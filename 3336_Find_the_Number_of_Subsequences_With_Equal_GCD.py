from collections import defaultdict


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        states = {(0, 0): 1}
        for value in nums:
            next_states = defaultdict(int)
            for (first_gcd, second_gcd), count in states.items():
                next_states[(first_gcd, second_gcd)] = (next_states[(first_gcd, second_gcd)] + count) % mod
                next_states[(gcd(first_gcd, value), second_gcd)] = (next_states[(gcd(first_gcd, value), second_gcd)] + count) % mod
                next_states[(first_gcd, gcd(second_gcd, value))] = (next_states[(first_gcd, gcd(second_gcd, value))] + count) % mod
            states = next_states

        result = 0
        for (first_gcd, second_gcd), count in states.items():
            if first_gcd and first_gcd == second_gcd:
                result = (result + count) % mod
        return result
