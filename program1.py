class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack:
                    return False
                top_element = stack.pop()
                if bracket_map[char] != top_element:
                    return False
        
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