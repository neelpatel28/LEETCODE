class Solution(object):
    def canAliceWin(self, n):
        turn = 10

        while n >= turn:
            n -= turn
            turn -= 1

        return turn % 2 == 1
