class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        minute_angle = minutes * 6.0
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360.0 - diff)


if __name__ == "__main__":
    sol = Solution()
    examples = [
        (12, 30),
        (3, 30),
        (3, 15),
    ]
    for hour, minutes in examples:
        print("hour=", hour, "minutes=", minutes, "angle=", sol.angleClock(hour, minutes))
