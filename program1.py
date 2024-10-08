class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop from stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the top element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the opening bracket onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets have been closed properly
        return not stack


# Taking input
s = input("Enter a string containing parentheses: ")

# Creating a Solution object and checking if the string is valid
solution = Solution()
result = solution.isValid(s)

# Output the result
if result:
    print("Output: true")
else:
    print("Output: false")
