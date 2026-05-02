class Solution:
    def rotatedDigits(self, n):
        """
        Count how many integers from 1 to n are 'good' numbers.
        A number is 'good' if after rotating each digit 180 degrees,
        we get a valid different number.
      
        Args:
            n: Upper bound of the range to check
          
        Returns:
            Count of good numbers in range [1, n]
        """
      
        def is_good_number(number):
            """
            Check if a number becomes a valid different number after rotation.
          
            Args:
                number: The number to check
              
            Returns:
                True if the number is good, False otherwise
            """
            rotated_number = 0
            temp_number = number
            place_value = 1
          
            # Process each digit from right to left
            while temp_number:
                digit = temp_number % 10
              
                # If digit cannot be rotated (3, 4, 7), number is invalid
                if rotation_map[digit] == -1:
                    return False
              
                # Build the rotated number digit by digit
                rotated_number = rotation_map[digit] * place_value + rotated_number
                place_value *= 10
                temp_number //= 10
          
            # Number is good if it changes after rotation
            return number != rotated_number
      
        # Mapping of each digit to its 180-degree rotation
        # -1 means the digit cannot be rotated to form a valid digit
        # Index represents the digit, value represents its rotation
        rotation_map = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        #               0  1  2   3   4   5  6   7   8  9
      
        # Count all good numbers from 1 to n
        return sum(is_good_number(i) for i in range(1, n + 1))