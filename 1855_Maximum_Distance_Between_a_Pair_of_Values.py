class Solution(object):
    def maxDistance(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        
        i = j = 0
        max_dist = 0

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if j - i > max_dist:
                    max_dist = j - i
                j += 1
            else:
                i += 1

        return max_dist