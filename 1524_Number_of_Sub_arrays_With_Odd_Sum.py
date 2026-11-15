class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even = 1
        odd = 0
        parity = 0
        ans = 0

        for num in arr:
            parity ^= num & 1

            if parity:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

            ans %= MOD

        return ans
