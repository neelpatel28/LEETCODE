class Solution:
    def checkDivisibility(self, n):
        temp = n
        digit_sum = 0
        digit_product = 1
        
        # Extract digits one by one
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
            
        # Check if original number is divisible by the combined total
        return n % (digit_sum + digit_product) == 0
