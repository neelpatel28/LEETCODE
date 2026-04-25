class Solution(object):
    def maxDistance(self, side, points, k):
        def to_perimeter(x, y):
            if y == 0:       return x
            elif x == side:  return side + y
            elif y == side:  return 2 * side + (side - x)
            else:            return 3 * side + (side - y)

        total = 4 * side
        pos = sorted(to_perimeter(x, y) for x, y in points)
        n = len(pos)
        # Double the array for circular handling
        doubled = pos + [p + total for p in pos]

        def can_place(d):
            import bisect
            for i in range(n):
                cur = pos[i]
                start = cur
                j = i
                count = 1
                while count < k:
                    target = cur + d
                    idx = bisect.bisect_left(doubled, target, j + 1, i + n)
                    if idx >= i + n:
                        break
                    cur = doubled[idx]
                    j = idx
                    count += 1
                if count == k and (start + total - cur) >= d:
                    return True
            return False

        lo, hi, ans = 1, total // k, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans