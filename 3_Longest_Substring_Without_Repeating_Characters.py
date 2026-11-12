class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        ans = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            ans = max(ans, right - left + 1)

        return ans
