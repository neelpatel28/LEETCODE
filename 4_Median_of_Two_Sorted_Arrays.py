class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            # Partition boundaries
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]

            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            # Correct partition found
            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2:
                    return max(left1, left2)

                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2.0

            # Too many elements taken from nums1
            elif left1 > right2:
                right = i - 1

            # Too few elements taken from nums1
            else:
                left = i + 1
