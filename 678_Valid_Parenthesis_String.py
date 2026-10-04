class Solution(object):
    def checkValidString(self, s):
        """:type s: str

        :rtype: bool
        """
        lo = hi = 0
        for c in s:
          if c == "(":
            lo += 1
            hi += 1
          elif c == ")":
            lo -= 1
            hi -= 1
          else:  # c == '*'
            lo -= 1
            hi += 1
          if hi < 0:
            break
          lo = max(lo, 0)
        return lo == 0
