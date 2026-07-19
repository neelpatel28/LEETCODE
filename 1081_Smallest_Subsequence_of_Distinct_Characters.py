class Solution(object):
    def smallestSubsequence(self, s):
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - 97] = i

        stack = []
        used = [False] * 26

        for i, c in enumerate(s):
            idx = ord(c) - 97

            if used[idx]:
                continue

            while stack and stack[-1] > c and last[ord(stack[-1]) - 97] > i:
                used[ord(stack.pop()) - 97] = False

            stack.append(c)
            used[idx] = True

        return ''.join(stack)