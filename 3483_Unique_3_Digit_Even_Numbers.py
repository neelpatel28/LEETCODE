class Solution(object):
    def totalNumbers(self, digits):
        available_counts = [0] * 10
        for d in digits:
            available_counts[d] += 1
            
        count = 0
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            needed = [0] * 10
            needed[d1] += 1
            needed[d2] += 1
            needed[d3] += 1
            
            if (available_counts[d1] >= needed[d1] and 
                available_counts[d2] >= needed[d2] and 
                available_counts[d3] >= needed[d3]):
                count += 1
                
        return count
