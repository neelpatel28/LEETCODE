class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0

        for num in arr1:
            left, right = 0, len(arr2)

            while left < right:
                mid = (left + right) // 2

                if arr2[mid] < num - d:
                    left = mid + 1
                else:
                    right = mid

            if left == len(arr2) or arr2[left] > num + d:
                count += 1

        return count
