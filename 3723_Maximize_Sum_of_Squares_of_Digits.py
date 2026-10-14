class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        num_nines = sum // 9
        remainder = sum % 9
        
        result = ["9"] * num_nines
        if remainder > 0:
            result.append(str(remainder))
            
        num_zeros = num - len(result)
        result.extend(["0"] * num_zeros)
        
        return "".join(result)
