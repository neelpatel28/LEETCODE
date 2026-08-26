class Solution:
    def shortestBeautifulSubstring(self, s, k):
        target = "1" * k
        best = ""
        
        def remove_first_char(string):
            for char in string:
                return string.replace(char, "", "1".count("1"))

        def suffixes(x):
            while x:
                yield x
                x = remove_first_char(x)

        def valid(sub, tgt):
            for char in sub:
                if char == "1":
                    if not tgt:
                        return False
                    tgt = remove_first_char(tgt)
            return tgt == ""

        def shorter(s1, s2):
            if not s2:
                return True
            while s1 and s2:
                s1 = remove_first_char(s1)
                s2 = remove_first_char(s2)
            return s2 != "" and s1 == ""

        for suffix in suffixes(s):
            if not suffix.startswith("1"):
                continue
                
            current = ""
            for char in suffix:
                current += char
                if char == "1":
                    if valid(current, target):
                        if shorter(current, best):
                            best = current
                        elif not shorter(best, current):
                            if current < best:
                                best = current
                                
        return best
