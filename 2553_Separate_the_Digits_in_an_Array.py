class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        
        return result