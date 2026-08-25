class Solution:
    def missingMultiple(self, nums, k):
        num_set = set(nums)
        i = 1
        while True:
            multiple = i * k
            if multiple not in num_set:
                return multiple
            i += 1
