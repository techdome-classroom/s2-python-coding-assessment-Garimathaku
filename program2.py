class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define a dictionary to map Roman numerals to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # Initialize total to 0
        total = 0

        # Loop through the string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            # Otherwise, add it to the total
            else:
                total += roman_map[s[i]]

        return total

# Taking input from the user
roman_numeral = input("Enter a Roman numeral: ")

# Create an instance of the Solution class
solution = Solution()

# Call the method to convert the Roman numeral to an integer and print the result
result = solution.romanToInt(roman_numeral)
print(f"Output: {result}")


