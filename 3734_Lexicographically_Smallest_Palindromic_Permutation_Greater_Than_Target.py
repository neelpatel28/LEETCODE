from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # 1. Check if a valid palindromic permutation is possible
        odd_count = sum(1 for char, count in counts.items() if count % 2 != 0)
        if odd_count > 1:
            return ""
            
        # 2. Extract mid_char if the string length is odd
        mid_char = ""
        left_counts = {}
        for char, count in counts.items():
            if count % 2 != 0:
                mid_char = char
            left_counts[char] = count // 2
            
        half_len = n // 2
        res_left = []
        
        # Helper to form the complete palindrome
        def build_palindrome(left_list):
            left_str = "".join(left_list)
            return left_str + mid_char + left_str[::-1]

        # 3. Backtracking function to build the left half of the palindrome
        def backtrack(idx, is_greater):
            if idx == half_len:
                full_pali = build_palindrome(res_left)
                # If we haven't strictly branched higher in the left half, 
                # we must verify the complete palindrome is greater than target.
                return full_pali if full_pali > target else ""
            
            # Find the starting character options
            start_char = 'a' if is_greater else target[idx]
            
            # Try available characters in sorted order to ensure lexicographical smallness
            for char in sorted(left_counts.keys()):
                if char >= start_char and left_counts[char] > 0:
                    left_counts[char] -= 1
                    res_left.append(char)
                    
                    next_greater = is_greater or (char > target[idx])
                    ans = backtrack(idx + 1, next_greater)
                    if ans:
                        return ans
                        
                    # Backtrack
                    res_left.pop()
                    left_counts[char] += 1
                    
            return ""
            
        return backtrack(0, False)
