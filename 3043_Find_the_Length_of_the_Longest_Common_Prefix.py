class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
        # Step 1: Store all prefixes of arr1
        prefix_set = set()
        
        for num in arr1:
            s = str(num)
            prefix = ""
            for ch in s:
                prefix += ch
                prefix_set.add(prefix)
        
        # Step 2: Check prefixes in arr2
        max_len = 0
        
        for num in arr2:
            s = str(num)
            prefix = ""
            
            for i, ch in enumerate(s):
                prefix += ch
                
                if prefix in prefix_set:
                    max_len = max(max_len, i + 1)
                else:
                    break   # important optimization
        
        return max_len