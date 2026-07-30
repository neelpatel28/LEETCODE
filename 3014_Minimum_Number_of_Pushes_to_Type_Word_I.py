class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        ans = 0
        for i in range(n):
            ans += i // 8 + 1
        return ans