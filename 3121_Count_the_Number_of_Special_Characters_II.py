class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = 0
        upper = 0
        invalid = 0

        for ch in word:
            bit = 1 << (ord(ch.lower()) - 97)

            if ch.islower():
                if upper & bit:
                    invalid |= bit
                lower |= bit
            else:
                if not (lower & bit):
                    invalid |= bit
                upper |= bit

        return bin((lower & upper) & ~invalid).count('1')