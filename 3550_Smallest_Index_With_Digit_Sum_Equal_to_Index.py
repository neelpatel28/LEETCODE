class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            # Sum the digits by converting the number to a string
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Since we iterate in order, the first match is the smallest index
            if digit_sum == i:
                return i
                
        return -1
