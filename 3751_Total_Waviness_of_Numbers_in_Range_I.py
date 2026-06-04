class Solution(object):
    def totalWaviness(self, num1, num2):
        
        def waviness(n):
            digits = list(map(int, str(n)))
            length = len(digits)
            
            if length < 3:
                return 0
            
            count = 0
            
            for i in range(1, length - 1):
                if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
                    count += 1
                elif digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                    count += 1
            
            return count
        
        total = 0
        
        for num in range(num1, num2 + 1):
            total += waviness(num)
        
        return total