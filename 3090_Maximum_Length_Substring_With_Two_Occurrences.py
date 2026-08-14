class Solution:
    def maximumLengthSubstring(self, s):
        counts = [0] * 26
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            idx = ord(char) - 97
            counts[idx] += 1
            
            while counts[idx] > 2:
                counts[ord(s[left]) - 97] -= 1
                left += 1
                
            if right - left + 1 > max_len:
                max_len = right - left + 1
                
        return max_len
