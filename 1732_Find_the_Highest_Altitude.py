class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        max_altitude = 0
        for net_gain in gain:
            altitude += net_gain
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestAltitude([-5, 1, 5, 0, -7]))  # Output: 1
    print(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Output: 0
