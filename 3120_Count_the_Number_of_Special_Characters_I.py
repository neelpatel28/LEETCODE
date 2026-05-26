class Solution(object):
    def numberOfSpecialChars(self, word):
        seen = [0] * 52
        
        for ch in word:
            if 'a' <= ch <= 'z':
                seen[ord(ch) - 97] = 1
            else:
                seen[ord(ch) - 65 + 26] = 1
        
        count = 0
        
        for i in range(26):
            if seen[i] and seen[i + 26]:
                count += 1
        
        return count