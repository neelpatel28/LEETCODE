class Solution:
    def stoneGameIX(self, stones):
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1
            
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
            
        return abs(cnt[1] - cnt[2]) > 2
