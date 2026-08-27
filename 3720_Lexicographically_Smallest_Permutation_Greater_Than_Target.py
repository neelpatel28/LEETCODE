from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        counts = Counter(s)
        
        matched_prefix = []
        for char in target:
            if counts[char] > 0:
                counts[char] -= 1
                matched_prefix.append(char)
            else:
                break
                
        for i in range(len(matched_prefix), -1, -1):
            if i < len(matched_prefix):
                counts[matched_prefix[i]] += 1
            
            if i == n:
                continue
                
            target_char = target[i]
            valid_chars = sorted([c for c in counts if c > target_char and counts[c] > 0])
            
            if valid_chars:
                chosen_char = valid_chars[0]
                counts[chosen_char] -= 1
                
                prefix = target[:i] + chosen_char
                suffix = "".join(sorted(counts.elements()))
                
                return prefix + suffix
                
        return ""
