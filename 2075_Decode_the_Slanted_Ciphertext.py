class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Step 1: Build matrix
        matrix = []
        idx = 0
        for i in range(rows):
            row = list(encodedText[idx:idx + cols])
            matrix.append(row)
            idx += cols
        
        # Step 2: Traverse diagonals
        result = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        # Step 3: Remove trailing spaces
        return ''.join(result).rstrip()