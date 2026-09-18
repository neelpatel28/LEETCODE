class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        valid_intervals = []
        for c in set(s):
            start = first[c]
            end = last[c]
            is_valid = True
            
            i = start
            while i <= end:
                curr_char = s[i]
                if first[curr_char] < start:
                    is_valid = False
                    break
                end = max(end, last[curr_char])
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))
                
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for start, end in valid_intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
                
        return res
